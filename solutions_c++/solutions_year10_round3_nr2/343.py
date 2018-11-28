#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
using namespace std;
const int MAX = (1<<7);
const int INFTY = (1<<30);

int nTestCases;
fstream	fin;
fstream fout;
int C;
long long L, P;

int minT[11][1001][1001];

inline void init(){
	fin >> L >> P >> C;
}


void main()
{
	fin.open("z:\\input.txt", ifstream::in);
	fout.open("z:\\output.txt", ifstream::out);


	memset(minT, 0, sizeof(minT));
	for(int C=2; C<=10; C++){
		for(int d=1; d<=999; d++)
			for(int l=1; l<=1000 && (l+d<=1000); l++){
				int p = l+d;
				if(p <= C*l)
					minT[C][l][p] = 0;
				else{
					int minC = INFTY;
					int minp;
					for(int p1=l+1; p1<p; p1++){
						int cost;
						cost = 1 + max(minT[C][l][p1], minT[C][p1][p]);
						if(minC > cost){
							minp = p1;
						}
						minC = min(minC, cost);
					}
					minT[C][l][p] = minC;
				}
			}
	}



	fin >> nTestCases;
	for(int testCase = 1; testCase <= nTestCases; testCase++){
		init();	
		fout << "Case #" << testCase <<": " << minT[C][L][P] << endl;
	}

	fin.close();
	fout.close();
}