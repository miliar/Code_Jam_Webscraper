// googlers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

bool find3tuple(int score, int P, bool& isSurprising)
{
	bool found = false, surprisingFound = false, normalFound = false;
	for(int p = P; p <= 10; ++p) {
		for(int  i = p-2; i <= p+2; ++i) {
			if(i < 0 || i > 10) 
				continue;
			for(int j = i-2; j <= i+2 ; ++j) {
				if(j < 0 || j > 10 || p - j > 2 || j - p > 2)
					continue;
				if(i + j == score - p) {
					found = true;
					if(i - j == 2 || j - i == 2 || i - p == -2 || p - i == 2 || p - j == 2 || j - p == 2)
						surprisingFound = true;
					else {
						normalFound = true;
						break;
					}
				}
				else if(i + j > score - p)
					break;
			}
			if(normalFound)
				break;
		}
		if(normalFound)
			break;
	}
	if(found) {
		if(normalFound)
			isSurprising = false;
		else 
			isSurprising = true;
	}
	
	return found;


}

int _tmain(int argc, _TCHAR* argv[])
{
	fstream f("in.txt", ios::in);
	fstream fout("out.txt", ios::out);
	int T;
	f >> T;
	for(int i = 1; i <= T; ++i) {
		int N, S, p;
		vector<int> score;
		f >> N >> S >> p;
		for(int j = 0; j < N; ++j) {
			int x;
			f >> x;
			score.push_back(x);
		}
		int dancers = 0;
		int numOfSurprising = 0;
		for(int j = 0; j < score.size(); ++j) {
			bool isSurprising = false;
			if(find3tuple(score[j], p, isSurprising) && (numOfSurprising <= S)) {
				if(isSurprising) { 
					if(numOfSurprising == S) // already reached the limit. can't count this one
						continue;
					++numOfSurprising;
				}
				++dancers;
			}
		}
		cout << "Case #" << i << ": " << dancers << endl;
		fout << "Case #" << i << ": " << dancers << endl;
	}
	return 0;
}

