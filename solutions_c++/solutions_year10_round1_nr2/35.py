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

int abs(int A) {
	if (A>0) return A;
	return -A;
	}


int main (void) {
//	fstream IN("B0.in", ios::in);	fstream OUT("B0.out", ios::out);
//	fstream IN("B1.in", ios::in);	fstream OUT("B1.out", ios::out);
	fstream IN("B2.in", ios::in);	fstream OUT("B2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		cout<<test<<"\n";
		int D,I,M,N;
		IN>>D>>I>>M>>N;
		
		vector <int> A(N);
		for (int i=0; i<N; i++) IN>>A[i];
		
		vector <vector <long long> > B(257, vector <long long> (N+1, 1000000000));
		B[256][0]=0;
		
		for (int i=0; i<N; i++) {
			//inserisci modificato
			for (int j=0; j<256; j++) {
				int start=max(0, j-M);
				int end=min(255, j+M);
				int cost=abs(j-A[i]);
				B[j][i+1]=B[256][i]+cost;
				for (int k=start; k<=end; k++) B[j][i+1]=min(B[j][i+1], B[k][i]+cost);
				}
			
			//cancella
			B[256][i+1]=B[256][i]+D;
			for (int j=0; j<256; j++) B[j][i+1]=min(B[j][i+1], B[j][i]+D);
			
			//inserisci falsi
			for (int j=0; j<256; j++) {
				for (int k=max(0, j-M); k<j; k++) B[j][i+1]=min(B[j][i+1], B[k][i+1]+I);
				}
			for (int j=255; j>=0; j--) {
				for (int k=j+1; k<=min(255, j+M); k++) B[j][i+1]=min(B[j][i+1], B[k][i+1]+I);
				}
			}
		
		long long MINI=1000000000;
		for (int i=0; i<257; i++) MINI=min(MINI, B[i][N]);
		
		OUT<<"Case #"<<test<<": "<<MINI<<"\n";
		}
	return 0;	
	}

