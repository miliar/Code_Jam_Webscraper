// GCJ_QR_B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int MaxNumberGooglers(string s){
	string MaxScoreStr;
	string NumberGooglersStr;
	string NumberSupStr;

	for (int i = 0; i < s.length(); i++){
		if (s[i] == ' '){
			s.replace(0, i+1, "");
			break;
		}
		else NumberGooglersStr += s[i];
	}

	for (int i = 0; i < s.length(); i++){
		if (s[i] == ' '){
			s.replace(0, i+1, "");
			break;
		}
		else NumberSupStr += s[i];
	}


	for (int i = 0; i < s.length(); i++){
		if (s[i] == ' '){
			s.replace(0, i+1, "");
			break;
		}
		else MaxScoreStr += s[i];
	}

	int MaxScore = atoi(MaxScoreStr.c_str());
	int NumberGooglers = atoi(NumberGooglersStr.c_str());
	int NumberSup = atoi(NumberSupStr.c_str());
	vector<int> TotalScores;

	s += " ";
	for (int j = 0; j < NumberGooglers; j++){
		string Score = "";
		for (int i = 0; i < s.length(); i++){
			if (s[i] == ' '){
				s.replace(0, i+1, "");
				TotalScores.push_back(atoi(Score.c_str()));
				break;
			}
			else Score += s[i];
		}
	}

	int Result = 0;

	for (int i = 0; i < TotalScores.size(); i++){
		if (TotalScores[i] - MaxScore - MaxScore - MaxScore >= 0){
			Result += 1;
		} else {
			if (TotalScores[i] - MaxScore - (MaxScore-1) - (MaxScore-1) >= 0 & (MaxScore-1) >= 0){
				Result += 1;
			}
			else {
				if (TotalScores[i] - MaxScore - (MaxScore-2) - (MaxScore-2) >= 0 & NumberSup > 0 & (MaxScore-2) >= 0){
					Result += 1;
					NumberSup -= 1;
				}
			}
		}
	}
	
	return Result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	string InputStr;
	int Output;
	ifstream myReadFile;
	myReadFile.open("B-large.in");
	ofstream myWriteFile;
	myWriteFile.open ("Output.txt");
	int case_num = 0;
	bool first = true;
	int NumberCases = 0;
	if (myReadFile.is_open()) {
		while (!myReadFile.eof()) {
			if (first){
				getline(myReadFile,InputStr);
				NumberCases = atoi(InputStr.c_str());
				first = false;
			}
			else {
				case_num += 1;
				if (case_num <= NumberCases){
					getline(myReadFile,InputStr);
					Output = MaxNumberGooglers(InputStr);
					myWriteFile << "Case #" << case_num << ": " << Output << endl;
				}
				else getline(myReadFile,InputStr);
			}
		}
	}
	myReadFile.close();
	myWriteFile.close();
	system ("pause");
	return 0;
}

