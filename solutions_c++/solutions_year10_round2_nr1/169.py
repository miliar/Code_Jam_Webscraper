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

string S[3000];
char buf[1020];

int main() {
	int t,tt,i,j,k,p, q;
	int N, M;
	FILE *fp = fopen("A.in", "r");
	FILE *fp1 = fopen("A.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		fscanf(fp,"%d%d\n",&N,&M);
		FOR(i,N) {
			fgets(buf, 1010, fp);
			buf[strlen(buf)-1] = '/';
			S[i] = string(buf);
		}
		p = 0;
		FOR(i,M) {
			q = 1;
			fgets(buf, 1010, fp);
			buf[strlen(buf)-1] = '/';
			S[N+i] = string(buf);
			FOR(k,N+i) {
				for(j=0;j<S[k].sz && j<S[N+i].sz;j++) if (S[k][j] != S[N+i][j]) break;
				if (j > q) q = j;
			}
			if (q != S[N+i].sz) {
				SFOR(j,q,S[N+i].sz) if (S[N+i][j] == '/') p++;
			}
		}
		fprintf(fp1,"Case #%d: %d\n", t+1, p);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}