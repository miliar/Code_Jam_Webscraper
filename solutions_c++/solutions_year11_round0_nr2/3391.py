#include <string>
#include <new>
#include <deque>
#include <bitset>
#include <cstring>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

class CombineRule {
	public:
		char A;
		char B;
		char C;
		CombineRule(char AT, char BT, char CT) {
			A = AT;
			B = BT;
			C = CT;
		}
};
class OppositionRule {
	public:
		char A;
		char B;
		OppositionRule(char AT, char BT) {
			A = AT;
			B = BT;
		}
};
//Divides String By Spaces
deque<string> Divide(string str)
{
	deque<string> Data;
	//for each space found
	int Count = 0;

	int pos = 0;
	while (str.find(" ",pos)!=string::npos){
		int st = str.find(" ",pos);
		Data.push_back(str.substr(pos, (st)-pos)); //Attach chars left of current space
		Count++; //Set Input for Next
		pos = str.find(" ",pos)+1; //Jump past current space
	}
	Data.push_back(str.substr(pos, str.length()-pos)); //Attach chars right of last space
	return Data;
}


int main()
{
	//arr is allocated
	ifstream Input("input.in");
	string Line;
	getline(Input, Line);
	int NumCases = atoi(Line.c_str());
	deque<string> Lines;
	for (int i=0; i<NumCases; i++) {
		getline(Input,Line);
		Lines.push_back(Line);
	}
	deque<deque<char> > CaseAns;
	for (int i=0; i<NumCases; i++) {
		deque<CombineRule> CRules;
		deque<OppositionRule> ORules;
		deque<char> Elements;
		deque<string> Data = Divide(Lines[i]);
		int C = atoi(Data[0].c_str());
		int Pos = 1;
		for (int j=0; j<C; j++) {
			//Create Combine Rules
			char A = Data[Pos].c_str()[0];
			char B = Data[Pos].c_str()[1];
			char C = Data[Pos].c_str()[2];
			CombineRule Rule(A, B, C);
			CRules.push_back(Rule);
			Pos++;
		}
		int D = atoi(Data[Pos].c_str());
		Pos++;
		for (int j=0; j<D; j++) {
			//Create Combine Rules
			char A = Data[Pos].c_str()[0];
			char B = Data[Pos].c_str()[1];
			OppositionRule Rule(A, B);
			ORules.push_back(Rule);
			Pos++;
		}
		Pos++;
		//Invoke
		for (int j=0; j<(int)strlen(Data[Pos].c_str()); j++) {
			Elements.push_back(Data[Pos].c_str()[j]);
			//Check Combination Rules
			bool Replaced = false;
			if (Elements.size()>1) {
				char A = Elements[Elements.size()-1];
				char B = Elements[Elements.size()-2];
				for (int k=0; k<(int)CRules.size(); k++) {
					if (A == CRules[k].A) {
						if (B == CRules[k].B) {
							Elements.pop_back();
							Elements.pop_back();
							Elements.push_back(CRules[k].C);
							Replaced = true;
						}
					}
					else if (A == CRules[k].B) {
						if (B == CRules[k].A) {
							Elements.pop_back();
							Elements.pop_back();
							Elements.push_back(CRules[k].C);
							Replaced = true;
						}
					}
				}
				//Check Opposition Rules
				if (Replaced == false) {
					for (int k=0; k<(int)ORules.size(); k++) {
						if (A == ORules[k].A) {
							for (int m=0; m<(int)Elements.size()-1; m++) {
								if (Elements[m] == ORules[k].B) {
									Elements.clear();
									break;
								}
							}
						}
						else if (A == ORules[k].B) {
							for (int m=0; m<(int)Elements.size()-1; m++) {
								if (Elements[m] == ORules[k].A) {
									Elements.clear();
									break;
								}
							}
						}
					}
				}
			}
		}
		CaseAns.push_back(Elements);
		cout << "Finished Case #" << i+1 << ": " << endl;
	}
	cout << "Starting Output" << endl;
	ofstream Output("output.in");
	for (int i=0; i<NumCases; i++) {
		Output << "Case #" << (i+1) << ": " << "[";
		for (int j=0; j<(int)CaseAns[i].size(); j++) {
			Output << CaseAns[i][j];
			if (j<(int)CaseAns[i].size()-1) {
				Output << ", ";
			}
		}
		Output << "]" << endl;
	}
	return(0);
}
