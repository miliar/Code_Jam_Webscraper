// NextNumber.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <set>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("E:\\Achiko\\codeJam\\B-large.in");
	ofstream fout("output.txt");

	int T;
	string S;

	fin >> T;
	for (int i=0; i<T; i++){		
		fin >> S;		
		int A[10];
		for (int k=0; k<10; k++){
			A[k] = 0;
		}

		int MinR;
		int cr = S.length()-1;
		while (cr>=0){
			int r = S[cr] - '0';
			A[r]++;
			S.erase(S.length()-1, 1);
			int z;
			for (z=r+1; z<=9; z++){
				if (A[z]>0) break;
			}
			if ((z<10) && (A[z]>0)) {
				MinR = z;
				break;
			}
			cr--;
		}
		fout << "Case #"<<(i+1)<<": ";
		if (cr<0){
			int z;
			for (z=1; z<=9; z++){
				if (A[z]>0) break;
			}
			A[z]--;
			fout<<z<<"0";

		} else {
			if (S.length()!=0){
				fout << S;
			}
			A[MinR]--;
			fout << MinR;
		}
		for (int z=0; z<=9; z++){
			for (int u=0; u<A[z]; u++){
				fout<<z;
			}
		}


		fout<<"\n";

	}

	fin.close();
	fout.close();

	return 0;
}

