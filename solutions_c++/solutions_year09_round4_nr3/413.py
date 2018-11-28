//code by Carlo Piovesan
//Google Code Jam, round 2, problem C

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

int COLOR[18];
bool possible[18][18];
vector <vector <bool> > A;
int NEXT[18];
int BEST;
int N;

void doit(int n) {
	if (n==N+1) return ;
//	cout<<n<<"\n";
//	for (int i=0; i<n; i++) cout<<COLOR[i]<<"\t";
//	system("PAUSE");
//	cout<<"\n";
	
	if (n==N) BEST=min(BEST, NEXT[N]);
	for (int i=0; i<N; i++) possible[n][i]=true;
	for (int i=0; i<n; i++) if (A[i][n]==false) possible[n][COLOR[i]]=false;
	for (int i=0; i<=NEXT[n]; i++) if (possible[n][i]) {
		COLOR[n]=i;
		NEXT[n+1]=max(NEXT[n], COLOR[n]+1);
		if (NEXT[n+1]<BEST) doit(n+1);
		}
	}


int main (void) {
	ofstream OUT;
	OUT.open ("OUT.txt");
	ifstream FILE("IN.txt");
	
	int Num;
	FILE>>Num;
	for (int ZZZ=1; ZZZ<=Num; ZZZ++) {
		int K;
		FILE>>N>>K;
		cout<<ZZZ<<"\n";
		vector <vector<int> > P(N, vector <int> (K));
		for (int i=0; i<N; i++) for (int j=0; j<K; j++) FILE>>P[i][j];
		
		A.resize(N, vector <bool> (N,true));
		for (int i=0; i<N; i++) for (int j=0; j<N; j++) if (i!=j) {
			A[i][j]=true;
			for (int k=0; k<K; k++) if (P[i][k]==P[j][k]) A[i][j]=false;
			for (int k=1; k<K; k++) if (((long long)P[i][k]-(long long)P[j][k])*((long long)P[i][k-1]-(long long)P[j][k-1])<0) A[i][j]=false;
			}
		
		for (int i=0; i<N; i++,cout<<"\n") for (int j=0; j<N; j++) cout<<A[i][j];
		
		BEST=1000;
		for (int i=0; i<=N; i++) NEXT[i]=1;
		COLOR[0]=0;
		doit(1);
		
		OUT<<"Case #"<<ZZZ<<": "<<BEST<<"\n";
//		system("PAUSE");
		}
	FILE.close();
	OUT.close();
	return 0;
	}
