#include <stdio.h>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define MP 10
using namespace std;
int P;
int M[MP+1][1<<MP], d[MP][1<<MP];
int c[MP][1<<MP][MP], _c[MP][1<<MP][MP];
int C(int lev, int p, int r)
{
	if (lev == P) return r>M[lev][p]?-1:0;
	if (_c[lev][p][r]) return c[lev][p][r];
	int re;
	_c[lev][p][r] = 1; c[lev][p][r] = -1;
	if (C(lev+1,p*2,r) != -1 && C(lev+1,p*2+1,r) != -1) {
		re = C(lev+1,p*2,r)+C(lev+1,p*2+1,r)+d[lev][p];
		if (c[lev][p][r] == -1 || c[lev][p][r] > re) c[lev][p][r] = re;
	}
	if (C(lev+1,p*2,r+1) != -1 && C(lev+1,p*2+1,r+1) != -1) {
		re = C(lev+1,p*2,r+1)+C(lev+1,p*2+1,r+1);
		if (c[lev][p][r] == -1 || c[lev][p][r] > re) c[lev][p][r] = re;
	}
//	printf("C(%d,%d,%d)=%d\n",lev,p,r,c[lev][p][r]);
	return c[lev][p][r];
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, i, j;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d",&P);
		for (i = 0; i < 1<<P; i++)
			scanf("%d",&M[P][i]);
		for (i = P-1; i >= 0; i--) {
			for (j = 0; j < 1<<i; j++)
				M[i][j] = max(M[i+1][j*2],M[i+1][j*2+1]);
		}
		for (i = P-1; i >= 0; i--) {
			for (j = 0; j < 1<<i; j++)
				scanf("%d",&d[i][j]);
		}
		memset(_c,0,sizeof(_c));
		printf("%d\n",C(0,0,0));
	}
	return 0;
}