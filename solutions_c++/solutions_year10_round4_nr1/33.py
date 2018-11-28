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

int A[400][400];
int SH[400], SV[400];

int F(int sx, int sy, int q, int w) {
	return abs(sx-q) + abs(sy-w) + 1;
}

int main() {
	int t,tt,i,j,k,p, q;
	int N, K,B,T;
	FILE *fp = fopen("A.in", "r");
	FILE *fp1 = fopen("A.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		fscanf(fp,"%d",&K);
		memset(A,0xFF,sizeof(A));
		memset(SH,0,sizeof(SH));
		memset(SV,0,sizeof(SV));
		FOR(i,K) {
			for(j=200-i;j<200+i+1;j+=2) fscanf(fp,"%d",&A[200-K+1+i][j]);
		}
		FORD(i,K-1) {
			for(j=200-i;j<200+i+1;j+=2) fscanf(fp,"%d",&A[200+K-1-i][j]);
		}
		SFOR(i,140,260) SFOR(j,140,260) if (A[i][j] != -1) {
			for(k=i-2;;k-=2) { if (A[k][j] == -1) break; if (A[k][j] != A[i][j]) SH[(i+k)/2] = 1; }
			for(k=i+2;;k+=2) { if (A[k][j] == -1) break; if (A[k][j] != A[i][j]) SH[(i+k)/2] = 1; }
			for(k=j-2;;k-=2) { if (A[i][k] == -1) break; if (A[i][k] != A[i][j]) SV[(j+k)/2] = 1; }
			for(k=j+2;;k+=2) { if (A[i][k] == -1) break; if (A[i][k] != A[i][j]) SV[(j+k)/2] = 1; }
		}
		p = 1000000;
		SFOR(i,140,260) SFOR(j,140,260) if ((SH[i] == 0) && (SV[j] == 0)) {
			q = 0;
			q = max(q,F(i,j,200-K+1,200));
			q = max(q,F(i,j,200+K-1,200));
			q = max(q,F(i,j,200,200-K+1));
			q = max(q,F(i,j,200,200+K-1));
			p = min(p,q);
		}
		fprintf(fp1,"Case #%d: %d\n", t+1, p*p - K*K);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}