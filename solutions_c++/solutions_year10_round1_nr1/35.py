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

int dx[4]={1,1,1,0};
int dy[4]={-1,0,1,1};

int main (void) {
//	fstream IN("A0.in", ios::in);	fstream OUT("A0.out", ios::out);
//	fstream IN("A1.in", ios::in);	fstream OUT("A1.out", ios::out);
	fstream IN("A2.in", ios::in);	fstream OUT("A2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;

	for (int test=1; test<=NUM_TEST; test++) {
		int N,K;
		IN>>N>>K;

		vector <string> A(N);
		for (int i=0; i<N; i++) IN>>A[i];
		for (int i=0; i<N; i++) cout<<A[i]<<"\n";
		
		for (int i=0; i<N; i++) {
			int kkk=N-1;
			for (int j=N-1; j>=0; j--) if (A[i][j]!='.') {
				A[i][kkk]=A[i][j];
				kkk--;
				}
			for (int j=kkk; j>=0; j--) A[i][j]='.';
			}
		
		cout<<"\n";
		for (int i=0; i<N; i++) cout<<A[i]<<"\n";

		
		vector <vector <char> > B(N+2, vector <char> (N+2, '.'));
		for (int i=0; i<N; i++) for (int j=0; j<N; j++) if (A[i][j]!='.') B[i+1][j+1]=A[i][j];
		
		for (int i=0; i<N+2; i++, cerr<<"\n") for (int j=0; j<N+2; j++) cerr<<B[i][j];
		
		
		bool red=false, blue=false;
		
		for (int i=1; i<=N; i++) for (int j=1; j<=N; j++) for (int d=0; d<4; d++) {
			bool f=true;
			char C=B[i][j];
			for (int m=1; (f) && (m<K); m++) {
				int ii=i+m*dx[d];
				int jj=j+m*dy[d];
				if (ii<0 || ii>=N+2) f=false;
				else if (j<0 || jj>=N+2) f=false;
				else if (B[ii][jj]!=C) f=false;
				}
			if (f==true && C=='R') red=true;
			if (f==true && C=='B') blue=true;
			}
		
		OUT<<"Case #"<<test<<": ";
		if (blue && red) OUT<<"Both";
		if (!blue && !red) OUT<<"Neither";
		if (!blue && red) OUT<<"Red";
		if (blue && !red) OUT<<"Blue";
		OUT<<"\n";
		}
	return 0;	
	}

