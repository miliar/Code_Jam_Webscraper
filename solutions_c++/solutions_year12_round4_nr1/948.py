#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int n, d[11111], r[11111], f[11111];
void solve() {
	scanf("%d", &n);
	for ( int i = 1; i <= n; i ++ ) 
		scanf("%d%d", &d[i], &r[i]);
	scanf("%d", &d[n+1]);
	r[n+1] = 0x3f3f3f3f;
	n ++;
	memset(f, 0, sizeof(f));
	f[1] = d[1];
	for ( int i = 1; i <= n; i ++ ) 
		if ( f[i] ) {
			for ( int j = i + 1; j <= n; j ++ ) {
				if ( d[j] - d[i] <= f[i] )
					f[j] = max(f[j], min(d[j] - d[i], r[j]));
			}
		}
	if ( f[n] != 0 ) 
		printf("YES\n");
	else
		printf("NO\n");
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int tst;
	scanf("%d", &tst);
	for ( int i = 1; i <= tst; i ++ ) {
		printf("Case #%d: ", i);
		solve();
	}
}
