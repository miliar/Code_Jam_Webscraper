//============================================================================
// Name        : bottrust.cpp
// Author      : Aziz
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream> //Standard input/output
#include <fstream> //File input/output
#include <cstdlib> //C library
#include <cmath> //Math library
#include <algorithm> //Some algorithms like sorting
#include <vector> //Vectors (Array lists)
#include <string> //Strings
#include <map> //Maps
#include <queue> //Maps

using namespace std;

ifstream fin ("bottrust.in");
ofstream fout ("bottrust.out");

queue<int> seqO, seqB, seq;
int T;
char tC;
int main() {
	fin >> T;
	for(int y = 0; y < T; y++){
		int N=0, tI=0, pO=0, pB=0, cT=0;
		fin >> N;
		for(int x=0; x < N; x++){
			fin >> tC >> tI;
			if(tC == 'O')
				seqO.push(tI-1);
			else
				seqB.push(tI-1);
			seq.push(tI-1);
		}
		while(!seq.empty()){
			if(seq.front() == seqO.front()){
				int cTi = abs(seqO.front() - pO) + 1;
				cT += cTi;
				pO = seq.front();
				seqO.pop();
				seq.pop();

				if(cTi >= abs(pB-seqB.front()))
					pB = seqB.front();
				else
					if(pB < seqB.front())
						pB += cTi;
					else if(pB > seqB.front())
						pB -= cTi;
			}
			else{
				int cTi = abs(seqB.front() - pB) + 1;
				cT += cTi;
				pB = seq.front();
				seqB.pop();
				seq.pop();

				if(cTi >= abs(pO-seqO.front()))
					pO = seqO.front();
				else
					if(pO < seqO.front())
						pO += cTi;
					else if(pO > seqO.front())
						pO -= cTi;
			}
		}
		fout << "Case #" << y+1 << ": " << cT << "\n";
	}
    system("PAUSE");
    return EXIT_SUCCESS;
}
