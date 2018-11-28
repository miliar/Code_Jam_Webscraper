#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;
#define maxl 4000010
#define INF 0x3f3f3f3f

int f[2][2][maxl], n, a[1000], mx;
int c[25];

void update(int& a, int b) {
	if(a < b) a = b;
}

int main()
{
	int t, sum, yi;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d", &n);
		mx = 0;
		sum = yi = 0;

		printf("Case #%d: ", q);

		for(int i=1; i<=n; ++i) {
			scanf("%d", &a[i]);
			mx = max(mx, a[i]);
			sum += a[i];
			yi ^= a[i];
		}

		int x = 1, idx = 0;
		while(x <= mx) x <<= 1;
		for(int i=0; i<=x; ++i) f[0][0][i] = f[1][0][i] = f[0][1][i] = f[1][1][i] = -INF;
		f[0][1][0] = 0;

		for(int i=1; i<=n; ++i) {
			idx ^= 1;
			for(int j=0; j<=x; ++j) {
				f[idx][0][j] = max( f[idx^1][0][j], f[idx^1][1][j] );
				f[idx][1][j] = -INF;
			}
			
			for(int j=0; j<=x; ++j) {
				//update(f[idx][j], f[idx^1][j]);
				if(f[idx^1][1][j] >= 0) {
					update(f[idx][1][j^a[i]], f[idx^1][1][j] + a[i]);
					//update(f[idx][0][j^a[i]], f[idx^1][0][j] + a[i]);
				}
				if(f[idx^1][0][j] >= 0) {
					update(f[idx][0][j^a[i]], f[idx^1][0][j] + a[i]);
				}
			}

			//for(int j=0; j<=x; ++j) printf("%d %d %d %d\n", i, j, f[idx][0][j], f[idx][1][j]);
			//puts("");
		}

		int ans = -INF;

		if(yi){ puts("NO"); continue; }

		for(int i=0; i<=x; ++i) ans = max(ans, f[idx][0][i]);

		if(ans > 0) printf("%d\n", ans);
		else puts("NO");
	}

	return 0;
}

