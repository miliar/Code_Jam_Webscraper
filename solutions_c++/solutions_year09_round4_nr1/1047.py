// ProblemC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <set>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("E:\\Achiko\\codeJam\\A-large(2).in");
	ofstream fout("output.txt");
	int T, N;
	fin >> T;

	for (int i=0; i<T; i++){
		fout << "Case #"<<(i+1)<<": ";
		fin >> N;
		char b;
		int ans = 0;
		vector<int> A = vector<int>(N, 0);
		for (int i=0; i<N; i++){
			int maxJ = -1;
			for (int j=0; j<N; j++){
				fin>>b;
				if (b=='1') {maxJ = j;
				}
			}
			A[i] = maxJ;
		}
		for (int i=0; i<N; i++){
			int j;
			for (j=0; j<A.size(); j++){
				if (A[j]<=i){
					break;
				}
			}
			ans = ans+j;
			A.erase(A.begin()+j, A.begin()+j+1);
		}


		fout<< ans <<"\n";

	}

	fin.close();
	fout.close();

	return 0;
}

