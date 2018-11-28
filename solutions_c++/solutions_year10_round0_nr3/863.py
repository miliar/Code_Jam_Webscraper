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

long long single_run(vector <long long> & A, int & index, long long K, long long N, long long & R) {
	R--;
	int start=index;
	long long euro=0;
	while (A[index]<=K) {
		K-=A[index];
		euro+=A[index];
		index=(index+1)%N;
		if (index==start) break;
		}
	return euro;
	}


int main (void) {
	fstream IN("C2.in", ios::in);
	fstream OUT("C2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		long long R,K,N;
		IN>>R>>K>>N;
		vector <long long> A(N);
		for (int i=0; i<N; i++) IN>>A[i];
		
		long long RESULT=0;
		int index=0;
		
		for (int i=0; i<N; i++) if (R>0) RESULT+=single_run(A, index, K, N, R);
		
		int start=index;
		long long ciclo=0;
		long long lunghezza_ciclo=0;
		if (R>0) do {
			lunghezza_ciclo++;
			ciclo+=single_run(A, index, K, N, R);
			} while (start!=index && R>0);
		
		RESULT+=ciclo;

		if (R>0) {
			while (R%lunghezza_ciclo!=0) RESULT+=single_run(A, index, K, N, R);
			RESULT+=ciclo*(R/lunghezza_ciclo);
			}
		
		OUT<<"Case #"<<test<<": "<<RESULT<<"\n";
		}
	return 0;	
	}

