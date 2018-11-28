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

//vector <vector <int> > A;
int A[200][200];
int B[200][200];

bool pure(int x, int y, int d) {
	for (int i=0; i<d; i++) for (int j=0; j<d; j++) if ((A[i+x][j+y]!=A[j+x][i+y]) || A[i+x][j+y]!=A[x+d-1-j][y+d-1-i]) return false;
	return true;
	}

int main (void) {
//	fstream IN("A0.in", ios::in);	fstream OUT("A0.out", ios::out);
//	fstream IN("A1.in", ios::in);	fstream OUT("A1.out", ios::out);
	fstream IN("A2.in", ios::in);	fstream OUT("A2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		int N;
		IN>>N;
//		cerr<<N<<"\n";
		
		int x=0, y=0;
		for (int i=0; i<N*2-1; i++) {
			int xx=x,yy=y;
			while (xx>=0 && yy<N) {
				IN>>A[xx][yy];
				xx--;
				yy++;
				}
			x++;
			if (x==N) {
				x--;
				y++;
				}
			}
		
//		for (int i=0; i<N; i++, cout<<"\n") for (int j=0; j<N; j++) cout<<A[i][j];
	
	
		int BEST=100000000;
	//cambiare un po' di cose
		
		
		vector <vector<bool> > X(4, vector <bool> (N));
		
		for (int t=0; t<4; t++) {
			for (int i=0; i<N; i++) for (int j=0; j<N; j++) B[i][j]=A[i][j];
			for (int i=0; i<N; i++) for (int j=0; j<N; j++) A[i][j]=B[N-1-j][i];
			
			
			for (int d=1; d<=N; d++) {
				bool f=true;
				for (int i=0; i<d && f; i++) for (int j=0; j<d && f; j++) {
					if (A[i][j]!=A[d-1-j][d-1-i]) f=false;
					}
				X[t][d-1]=f;
				}
			}
		
		for (int t=0; t<4; t++) {
			for (int i=0; i<N; i++) for (int j=0; j<N; j++) if (X[t][i] && X[(t+1)%4][j])BEST=min(BEST, N+N+N-i-j-2);
			}
				
//		cout<<N<<"\t"<<BEST*BEST-N*N<<"\n";
		OUT<<"Case #"<<test<<": "<<(BEST*BEST-N*N)<<"\n";
		}
	return 0;	
	}

