#include<stdio.h>
#include<string.h>
#define maxn 8

int t[maxn], sol[maxn], OK[maxn], P[maxn];


int main() {

	int tt;
	freopen("b-dance.in","r", stdin);
	freopen("b-dance.out", "w", stdout);
	scanf("%d", &tt); 
	for( int ii = 1; ii <= tt; ++ii) {
		printf("Case #%d: ", ii);
		int maxim = 0;
		int n, s, min;
		scanf("%d %d %d", &n, &s, &min);
		memset( OK, 0, sizeof(OK));
		memset( P, 0, sizeof(P));
		memset( sol, 0, sizeof(sol));
		for( int i = 1; i <= n; ++i) {
			scanf("%d", &t[i]);
			for( int k = 0; k <= t[i]/3 && k <= 10; k++)
				for( int l = k; l+k <= t[i] && l <= 10 && l <= k + 2; l++) {
					int j = t[i] - k - l;
					if( j < k ) continue;
					if( j > 10 ) continue;
					if( j - 2 > k ) continue;
					if( j - 2 == k ) {
						P[i] = 1;
						if( j >= min )
							OK[i] = 1;
					}
					if( j - k <= 1 ) {
						if( j >= min )
							sol[i] = 1;
					}
				}
		}
		for( int k = 0; k < (1 << n); ++k) {
			int cate = 0, nasol = 0, nr = 0;
			for( int j = 0; j < n; ++j) {
				if( (1<<j) & k ) {
					if( P[j+1] == 0) {
						nasol = 1;
						break;
					}
					nr++;
					cate += OK[j+1];
				}
				else cate += sol[j+1];
			}
			if( nasol ) continue;
			if( nr != s ) continue;
			if( cate > maxim )
				maxim = cate;
		}
		
		printf("%d\n", maxim);
		
	}
	
	
	return 0;
}
