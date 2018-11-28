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

int A[2][400][400];

int main() {
	int t,tt,i,j,k,p,q;
	int N, K,B,T;
	int x1, x2, y1, y2;
	FILE *fp = fopen("C.in", "r");
	FILE *fp1 = fopen("C.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		fscanf(fp,"%d",&K);
		memset(A,0,sizeof(A));
		FOR(k,K) {
			fscanf(fp,"%d%d%d%d",&x1,&y1,&x2,&y2);
			SFOR(i,x1,x2+1) SFOR(j,y1,y2+1) A[0][i][j] = 1;
		}
		p = 0;
		q = 0;
		bool f = true;
		while (f) {
			f = false;
			q++;
			memset(A[1-p], 0, sizeof(A[1-p]));
			SFOR(i,1,200) SFOR(j,1,200) if ((A[p][i][j] == 1) && ((A[p][i-1][j] == 1) || (A[p][i][j-1] == 1))) { f = true; A[1-p][i][j] = 1; }
			SFOR(i,1,200) SFOR(j,1,200) if ((A[p][i-1][j] == 1) && (A[p][i][j-1] == 1)) { f = true; A[1-p][i][j] = 1; }
			p = 1-p;
		}
		fprintf(fp1,"Case #%d: %d\n", t+1, q);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}