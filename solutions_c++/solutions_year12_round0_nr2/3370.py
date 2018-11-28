//Template for Google Code Contest
#include <iostream>
#include <fstream>
#include <string>
#include <new>
#include <vector>
#include <bitset>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <algorithm>
#include<math.h>
using namespace std;

//Divides String By Spaces
vector<string> Divide(string str)
{
	vector<string> Data;
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

string ltoa(long X) {
	 stringstream ss;//create a stringstream
	 ss << X;//add number to the stream
	 return ss.str();//return a string with the contents of the stream
}

bool Descending(int i,int j) {
	return (i > j);
}

int MatchBest(int Total) {
	return ceil(Total / 3.0);
}

int MatchSurprise(int Total) {
	return ceil((Total + 2)/ 3.0);
}
int main()
{
	//arr is allocated
	ifstream Input("input.in");
	string Line;
	getline(Input, Line);
	int NumCases = atoi(Line.c_str());
	vector<string> Lines;
	vector<long> Out;
	for (int i=0; i < NumCases; i++) {
		getline(Input,Line);
		Lines.push_back(Line);
	}
	for (int i=0; i < NumCases; i++) {
		vector<string> Data = Divide(Lines[i]);
		int N = atoi(Data[0].c_str());
		int S = atoi(Data[1].c_str());
		int p = atoi(Data[2].c_str());
		vector<int> Totals;
		for (int j=0; j < N; j++) {
			Totals.push_back(atoi(Data[j + 3].c_str()));
		}
		sort(Totals.begin(), Totals.end());
		int MaxBest = 0;
		int SLeft = S;
		for (int j=Totals.size()-1; j >= 0; j--) {
			//cout << Totals[j] << " ";
			if (Totals[j] >= 28) {
				MaxBest++;
			}
			else if (Totals[j] >= 2) {
				if (MatchBest(Totals[j]) >= p) {
					MaxBest++;
				}
				else if (MatchSurprise(Totals[j]) >= p) {
					if (SLeft != 0) {
						MaxBest++;
						SLeft--;
					}
					else {
						break;
					}
				}
			}
			else if (Totals[j] == 1) {
				if (p <= 1) {
					MaxBest++;
				}
			}
			if (Totals[j] == 0) {
				if (p == 0) {
					MaxBest++;
				}
			}
		}
		Out.push_back(MaxBest);
		cout << "Finished Case #:" << i+1 << endl;
	}
	cout << "Starting Output" << endl;
	ofstream Output("output.in");
	for (int i=0; i < NumCases; i++) {
		Output << "Case #" << i + 1 << ": " << Out[i] << endl;
	}
	return(0);
}
