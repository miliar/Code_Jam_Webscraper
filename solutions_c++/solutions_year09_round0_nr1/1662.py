// GCJ2009_Qualification.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

bool identity (bool b) { return b; }


void task1(const char* in_filename, const char* out_filename)
{
	ifstream in(in_filename);
	ofstream out(out_filename);
	if (in.is_open())
	{
		unsigned int L, D, N;
		in >> L >> D >> N;
		// L - letters, D - words, N - cases
		vector<string> allWords(D), allPatterns(N);
		for (unsigned int i = 0; i < D; ++i)
			in >> allWords[i];
		for (unsigned int i = 0; i < N; ++i)
			in >> allPatterns[i];
		for (unsigned int caseNumber = 1; caseNumber <= N; ++caseNumber) {
			vector<bool> possibleWordsNumbers(D, true);
			//for (unsigned int i = 0; i < D; ++i) {
			//	possibleWordsNumbers.insert(i);
			//}
			string& pattern = allPatterns[caseNumber - 1];
			unsigned int positionInPattern = 0;
			for (unsigned int letter = 0; letter < L; ++letter) {
				
				set<char> letterChars;
				if (pattern[positionInPattern] != '(') {
					letterChars.insert(pattern[positionInPattern]);
					++positionInPattern;
				}
				else {
					++positionInPattern;
					while(pattern[positionInPattern] != ')') {
						letterChars.insert(pattern[positionInPattern]);
						++positionInPattern;
					}
					++positionInPattern;
				}
				
				for (unsigned int wordNumber = 0; wordNumber < D; ++wordNumber) {
					if (letterChars.find(allWords[wordNumber][letter]) == letterChars.end()) {
						possibleWordsNumbers[wordNumber] = false;
					}
				}								
			}
			out << "Case #" << caseNumber << ": " 
					<< count_if(possibleWordsNumbers.begin(), possibleWordsNumbers.end(), identity) << endl;
		}
	}
	else
	{
		throw "File not found";
	}
	in.close();
	out.close();
}


int _tmain(int argc, _TCHAR* argv[])
{
	task1("A-small-attempt0.in", "A-small.out");
	return 0;
}

