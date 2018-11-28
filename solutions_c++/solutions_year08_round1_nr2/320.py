#include <stdio.h>
#include <string.h>

int res;
int L[10], P[100][10], out[10], M[10], min;
int n, m;
		
void solve(int step, int L[]) {
	if( step == n ) {
		int chk = 1;
		for(int i = 0; i < m && chk; i++) {
			int t = 0;
			for(int j = 0; j < n; j++) {
				if( P[i][j] == -1 ) continue;
				if( P[i][j] == L[j] ) t++;
			}
			if( t == 0 ) chk = 0;
		}
		if( !chk ) return;
		res = 1;
		
		int c = 0;
		for(int i = 0; i < n; i++)
			if( L[i] == 1 ) c++;
		if( c < min ) {
			min = c;
		
			for(int i = 0; i < n; i++)
				out[i] = L[i];
		}
		return;
	}
	L[step] = 0;
	solve(step + 1, L);
	L[step] = 1;
	solve(step + 1, L);
}
int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int ZZ;
	scanf("%d", &ZZ);
	for(int zz = 1; zz <= ZZ; zz++) {
		memset(L, -1, sizeof L);
		memset(P, -1, sizeof P);
		memset(out, -1, sizeof out);
		min = 1<<30;
		res = 0;
		scanf("%d %d", &n, &m);
		int chk = 1;
		for(int i  =0 ; i < m && chk; i++) {
			int t, x, y;
			scanf("%d", &t);
			for(int j = 0; j < 10; j++) 
				P[i][j] = -1;
			for(int j = 0; j < t && chk; j++) {
				scanf("%d %d", &x, &y);
				P[i][x-1] = y;
			}
		}
		solve(0, L);

		if( !res ) printf("Case #%d: IMPOSSIBLE\n", zz);
		else {
			printf("Case #%d: ", zz);
			for(int i = 0; i < n; i++) {
				printf("%d ", out[i]);
			}
			printf("\n");
		}
	}
	return 0;
}