//code by Carlo Piovesan
//Google Code Jam, round 2, problem D

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

double pow2(int A) {
	return (double)A*A;
	}

int main (void) {
	ofstream OUT;
	OUT.open ("OUT.txt");
	ifstream FILE("IN.txt");
	
	int Num;
	FILE>>Num;
	for (int ZZZ=1; ZZZ<=Num; ZZZ++) {
		int N;
		FILE>>N;
		vector <int> X(N),Y(N),R(N);
		for (int i=0; i<N; i++) FILE>>X[i]>>Y[i]>>R[i];
		
		
		
		long long RES;
		long long K=10000000;
		if (N==1) RES=R[0]*K;
		else if (N==2) {
			RES=max(R[0],R[1])*K;
			}
		else if (N==3) {
			double A=1000000;
			A=min(A, max((double)R[0], (double)0.5*(R[1]+R[2]+sqrt(pow2(X[2]-X[1])+pow2(Y[2]-Y[1])))));
			A=min(A, max((double)R[1], (double)0.5*(R[0]+R[2]+sqrt(pow2(X[2]-X[0])+pow2(Y[2]-Y[0])))));
			A=min(A, max((double)R[2], (double)0.5*(R[0]+R[1]+sqrt(pow2(X[0]-X[1])+pow2(Y[0]-Y[1])))));
			A*=K;
			RES=(long long)A;
			}
		else system("PAUSE");
		
		OUT<<"Case #"<<ZZZ<<": "<<RES/K<<".";
		while (K>1) {
			RES%=K;
			K/=10;
			OUT<<RES/K;
			}
		OUT<<"\n";
		}
	FILE.close();
	OUT.close();
	return 0;
	}
