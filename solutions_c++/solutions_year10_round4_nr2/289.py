#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <math.h>
#include <bitset>
#include <ctime>
#include <sys/time.h>

using namespace std;

long long A[2000][15];
const long long INF=(long long)10000000*100000;

int main (void) {
//	fstream IN("B0.in", ios::in);	fstream OUT("B0.out", ios::out);
//	fstream IN("B1.in", ios::in);	fstream OUT("B1.out", ios::out);
	fstream IN("B2.in", ios::in);	fstream OUT("B2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		int P;
		IN>>P;
		
		int N=1<<P;
		
		for (int i=0; i<N; i++) {
			int m;
			IN>>m;
			m=P-m;
			for (int j=0; j<m; j++) A[i][j]=INF;
			for (int j=m; j<15; j++) A[i][j]=0;
			}
		
		for (int d=1; d<N; d*=2) {
			for (int i=0; i<N; i+=d+d) {
				for (int j=0; j<15; j++) A[i][j]+=A[i+d][j];
				for (int j=0; j<15; j++) A[i][j]=min(A[i][j], INF);
				int cost;
				IN>>cost;
//				cout<<i<<"\t"<<i+d<<"\t"<<cost<<"\n";
				for (int j=0; j+1<15; j++) A[i][j]=min(A[i][j], A[i][j+1]+cost);
				}
			}
		
		OUT<<"Case #"<<test<<": "<<A[0][0]<<"\n";
		}
	return 0;	
	}

