#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

#define lint long long

#define sz size()
#define pb push_back

#define FOR(i,n) SFOR(i,0,n)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

lint FF[1500][15][15];
int C[1500][15];

lint F(int q, int w, int m) {
	if (FF[q][w][m] == -1) {
		FF[q][w][m] = min(F(q,w-1,m) + F(q+(1<<(w-1)),w-1,m), F(q,w-1,m+1) + F(q+(1<<(w-1)),w-1,m+1) + C[q][w]);
	}
	return FF[q][w][m];
}

int M[1500];

int main() {
	int t,tt,i,j,k,p,q;
	int N, K,B,T;
	int x1, x2, y1, y2;
	FILE *fp = fopen("B.in", "r");
	FILE *fp1 = fopen("B.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		memset(FF,0xFF,sizeof(FF));
		fscanf(fp,"%d",&N);
		FOR(i,(1<<N)) FOR(j,15) FF[i][0][j] = 1000000000;
		FOR(i,(1<<N)) fscanf(fp,"%d", &M[i]);
		FOR(i,(1<<N)) SFOR(j,max(N-M[i],0),15) FF[i][0][j] = 0;
		SFOR(j,1,N+1) for(i=0;i<(1<<N);i+=(1<<j)) fscanf(fp, "%d", &C[i][j]);
		fprintf(fp1,"Case #%d: %lld\n", t+1, F(0,N,0));
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}