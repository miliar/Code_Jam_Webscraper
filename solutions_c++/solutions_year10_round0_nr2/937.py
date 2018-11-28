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

int A[1010][100];
int sa[1010];

int main() {
	int t,tt,i,j,k,p, q;
	char buf[100];
	FILE *fp = fopen("B.in", "r");
	FILE *fp1 = fopen("B.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		memset(A,0,sizeof(A));
		fscanf(fp,"%d",&k);
		p = 0;
		FOR(j,k) {
			fscanf(fp,"%s",buf);
			FOR(i,strlen(buf)) A[p][strlen(buf)-1-i] = buf[i] - '0';
			sa[p] = strlen(buf);
			FOR(q,p) { if (sa[q] != sa[p]) continue; FOR(i,sa[q]) if (A[p][i] != A[q][i]) break; if (i == sa[q]) break; }
			if (q != p) p--;
			p++;
		}
		k = p;
//		FOR(i,k) { FORD(j,sa[i]) printf("%d",A[i][j]); printf("\n"); } printf("\n");
		FOR(j,k-1) {
			if (sa[j] > sa[j+1]) i = 0; else if (sa[j] < sa[j+1]) i = 1; else
				FORD(p, sa[j]) if (A[j][p] > A[j+1][p]) { i = 0; break; } else if (A[j][p] < A[j+1][p]) { i = 1; break; }
			if (i == 0) {
				FOR(i,sa[j]) A[j][i] -= A[j+1][i];
			} else {
				FOR(i,sa[j+1]) A[j][i] = A[j+1][i] - A[j][i];
				sa[j] = sa[j+1];
			}
			FOR(i,sa[j]) if (A[j][i] < 0) { A[j][i] += 10; A[j][i+1]--; }
			while ((sa[j] > 0) && (A[j][sa[j]-1] == 0)) sa[j]--;
		}
//		FOR(i,k) { FORD(j,sa[i]) printf("%d",A[i][j]); printf("\n"); } printf("\n");
		FOR(j,k-2) {
			while ((sa[j] != 0) && (sa[j+1] != 0)) 
			{
				if (sa[j] > sa[j+1]) i = 0; else if (sa[j] < sa[j+1]) i = 1; else
					FORD(p, sa[j]) if (A[j][p] > A[j+1][p]) { i = 0; break; } else if (A[j][p] < A[j+1][p]) { i = 1; break; }
				if (i == 0) {
					p = max(sa[j] - sa[j+1] - 1, 0);
					FOR(i,sa[j+1]) A[j][i+p] -= A[j+1][i];
					FOR(i,sa[j]) if (A[j][i] < 0) { A[j][i] += 10; A[j][i+1]--; }
					while ((sa[j] > 0) && (A[j][sa[j]-1] == 0)) sa[j]--;
				} else {
					p = max(sa[j+1] - sa[j] - 1, 0);
					FOR(i,sa[j]) A[j+1][i+p] -= A[j][i];
					FOR(i,sa[j+1]) if (A[j+1][i] < 0) { A[j+1][i] += 10; A[j+1][i+1]--; }
					while ((sa[j+1] > 0) && (A[j+1][sa[j+1]-1] == 0)) sa[j+1]--;
				}
			}
			if (sa[j+1] == 0) {
				sa[j+1] = sa[j];
				FOR(i,sa[j]) A[j+1][i] = A[j][i];
			}
		}
//		FOR(i,k) { FORD(j,sa[i]) printf("%d",A[i][j]); printf("\n"); } printf("\n");
		j = k-2;
		while ((sa[j] != 0) && (sa[j+1] != 0)) 
		{
			if (sa[j] > sa[j+1]) i = 0; else if (sa[j] < sa[j+1]) i = 1; else
				FORD(p, sa[j]) if (A[j][p] > A[j+1][p]) { i = 0; break; } else if (A[j][p] < A[j+1][p]) { i = 1; break; }
			if (i == 0) {
				break;
			} else {
				p = max(sa[j+1] - sa[j] - 1, 0);
				FOR(i,sa[j]) A[j+1][i+p] -= A[j][i];
				FOR(i,sa[j+1]) if (A[j+1][i] < 0) { A[j+1][i] += 10; A[j+1][i+1]--; }
				while ((sa[j+1] > 0) && (A[j+1][sa[j+1]-1] == 0)) sa[j+1]--;
			}
		}
		if (sa[j+1] == 0) j++;
		else
		{
			FOR(i,sa[j]) A[j][i] -= A[j+1][i];
			FOR(i,sa[j]) if (A[j][i] < 0) { A[j][i] += 10; A[j][i+1]--; }
			while ((sa[j] > 0) && (A[j][sa[j]-1] == 0)) sa[j]--;
		}
		if (sa[j] == 0) sa[j] = 1;
		fprintf(fp1, "Case #%d: ", t+1); FORD(i,sa[j]) fprintf(fp1,"%d", A[j][i]); fprintf(fp1,"\n");
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}