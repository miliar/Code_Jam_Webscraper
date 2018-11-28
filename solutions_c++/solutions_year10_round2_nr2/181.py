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

int X[1000], V[1000];

int main() {
	int t,tt,i,j,k,p, q;
	int N, K,B,T;
	FILE *fp = fopen("B.in", "r");
	FILE *fp1 = fopen("B.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		fscanf(fp,"%d%d%d%d",&N,&K,&B,&T);
		FOR(i,N) fscanf(fp,"%d",&X[i]);
		FOR(i,N) fscanf(fp,"%d",&V[i]);
		reverse(X,X+N);
		reverse(V,V+N);
		j = 0;
		FOR(i,N) { if (X[i] + T*V[i] >= B) K--; else j += K; if (K == 0) break; }
		if (K != 0) fprintf(fp1,"Case #%d: IMPOSSIBLE\n", t+1); else fprintf(fp1,"Case #%d: %d\n", t+1, j);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}