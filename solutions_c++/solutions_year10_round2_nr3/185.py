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


int FF[1000][1000];
int C[1000][1000];

int F(int q, int w) {
	if (FF[q][w] != -1) return FF[q][w];
	int i, j = 0;
	SFOR(i,1,w) j = (j + (F(w,i)*(lint)C[q-w-1][w-i-1])%100003)%100003;
	FF[q][w] = j;
	return j;
}

int main() {
	int t,tt,i,j,k,p, q;
	int N, M;
	FOR(i,1000) { C[0][i] = 0; C[i][0] = 1; }
	SFOR(i,1,1000) SFOR(j,1,1000) C[i][j] = (C[i-1][j] + C[i-1][j-1])%100003;
	FILE *fp = fopen("C.in", "r");
	FILE *fp1 = fopen("C.out", "w");
	fscanf(fp, "%d", &tt);
	memset(FF,0xFF,sizeof(FF));
	FOR(i,1000) FF[i][1] = 1;
	FOR(t,tt) {
		fscanf(fp,"%d",&N);
		q = 0;
		SFOR(i,1,N) q = (q+F(N,i))%100003;
		fprintf(fp1,"Case #%d: %d\n", t+1, q);
	}
	printf("%d\n",FF[5][0]);
	fclose(fp);
	fclose(fp1);
	return 0;
}