// alien.cpp : Defines the entry point for the console application.
//
#define maxD 5000
#define maxL 15

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <set>
using namespace std;

int main(int argc, char* argv[])
{

	ifstream fin("E:\\Achiko\\codeJam\\alien\\alien\\t2.in");
	ofstream fout("output.txt");
	
	string dict[maxD];
	int L, D, N;
	fin >> L >> D >> N;
	for (int i=0; i<D; i++){		
		fin >> dict[i];		
	}
	
	string line;

	for (int k=1; k<=N; k++){
		fin >> line;

		vector<int> A;
		for (int i=0; i<D; i++){
			A.push_back(i);
		}

		int charN = 0;
		int i=0;
		while (i<line.length()){
			set<char> S;
			if (line[i]=='('){
				i++;
				while ((line[i]!=')') && (i<line.length())){
					S.insert(line[i]);
					i++;
				}
				i++;
				
			} else {
				S.insert(line[i]);
				i++;
			}
			vector<int> B;
			for (int z=0; z<A.size(); z++){
				if ( S.find(dict[A[z]][charN])!=S.end()){
					B.push_back(A[z]);
				}
			}
			A = B;
			charN++;
		}
		fout << "Case #"<<k<<": "<<A.size()<<"\n";

	}
	fin.close();
	fout.close();

	return 0;
}

