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
		long Pairs = 0;
		vector<string> Data = Divide(Lines[i]);
		long A = atol(Data[0].c_str());
		long B = atol(Data[1].c_str());
		for (long j = A; j < B; j++) {
			string Orig = ltoa(j);
			cout << Orig << " ";
			for (long k = 0; k < Orig.length() - 1; k++) {
				string Recycled = "";
				if  ((Orig.length() - k - 1) != 0) {
					Recycled += Orig.substr(k + 1, Orig.length() - k - 1);
				}
				if (k !=0) {
					Recycled += Orig.substr(0, k);
				}
				Recycled += Orig.substr(k, 1);
				long Trim = 0;
				for (long l=0; l < Recycled.length(); l++) {
					if ((Recycled.c_str())[l] == '0') {
						Trim++;
					}
					else {
						break;
					}
				}
				Recycled = Recycled.substr(Trim, Recycled.length() - Trim);
				cout << Recycled;
				if (Recycled.length() == ltoa(j).length()) {
					if ((atol(Recycled.c_str()) > A) && (atol(Recycled.c_str()) <= B) && (atol(Recycled.c_str()) > j))  {
						Pairs++;
						cout << "*";
					}
				}
				cout << " ";
			}
			cout << endl;
		}
		Out.push_back(Pairs);
		cout << "Finished Case #:" << i+1 << endl;
	}
	cout << "Starting Output" << endl;
	ofstream Output("output.in");
	for (int i=0; i < NumCases; i++) {
		Output << "Case #" << i + 1 << ": " << Out[i] << endl;
	}
	return(0);
}
