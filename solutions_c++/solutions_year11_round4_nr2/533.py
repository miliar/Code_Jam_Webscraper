/*
 * =========================================================
 *       Filename:  B.cpp
 *    Description:  
 *        Created:  2011/6/4 23:17:26
 *         Author:  rocket323
 * =========================================================
 */
#include <stdio.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#define maxl 600
#define ll long long
using namespace std;

ll sx[maxl][maxl], sy[maxl][maxl], s[maxl][maxl];
ll n, m, w[maxl][maxl];
char str[maxl][maxl];

bool check(ll i, ll j, ll k) {
	if(k % 2 == 1) {
		ll tsx = sx[i][j] - sx[i-k][j] - sx[i][j-k] + sx[i-k][j-k];
		ll tsy = sy[i][j] - sy[i-k][j] - sy[i][j-k] + sy[i-k][j-k];
		ll sm = s[i][j] - s[i-k][j] - s[i][j-k] + s[i-k][j-k];
		ll x0 = i - k / 2, y0 = j - k / 2;

		ll tx = tsx - x0 * sm;
		tx -= (i - x0) * (w[i][j] + w[i][j-k+1]);
		tx -= (i - k + 1 - x0) * (w[i-k+1][j] + w[i-k+1][j-k+1]);

		ll ty = tsy - y0 * sm;
		ty -= (j - y0) * (w[i][j] + w[i-k+1][j]);
		ty -= (j - k + 1 - y0) * (w[i][j-k+1] + w[i-k+1][j-k+1]);

		return tx == 0 && ty == 0;
	}
	else {
		ll tsx = sx[i][j] - sx[i-k][j] - sx[i][j-k] + sx[i-k][j-k];
		ll tsy = sy[i][j] - sy[i-k][j] - sy[i][j-k] + sy[i-k][j-k];
		ll sm = s[i][j] - s[i-k][j] - s[i][j-k] + s[i-k][j-k];
		ll x0 = 2 * i - k + 1, y0 = 2 * j - k + 1;

		ll tx = 2 * tsx - x0 * sm;
		tx -= (2 * i - x0) * (w[i][j] + w[i][j-k+1]);
		tx -= (2 * (i - k + 1) - x0) * (w[i-k+1][j] + w[i-k+1][j-k+1]);

		ll ty = 2 * tsy - y0 * sm;
		ty -= (2 * j - y0) * (w[i][j] + w[i-k+1][j]);
		ty -= (2 * (j - k + 1) - y0) * (w[i][j-k+1] + w[i-k+1][j-k+1]);

		return tx == 0 && ty == 0;
	}
}

int main() {
	ll t, d;
	scanf("%I64d", &t);
	for(ll q=1; q<=t; ++q) {
		scanf("%I64d%I64d%I64d", &n, &m, &d);
		for(ll i=0; i<n; ++i) scanf("%s", str[i]);
		for(ll i=1; i<=n; ++i) {
			for(ll j=1; j<=m; ++j) w[i][j] = str[i-1][j-1] - '0';
		}
		memset(s, 0, sizeof s);
		memset(sx, 0, sizeof sx);
		memset(sy, 0, sizeof sy);
		for(ll i=1; i<=n; ++i) {
			for(ll j=1; j<=m; ++j) {
				s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + w[i][j];
				sx[i][j] = sx[i-1][j] + sx[i][j-1] - sx[i-1][j-1] + i * w[i][j];
				sy[i][j] = sy[i-1][j] + sy[i][j-1] - sy[i-1][j-1] + j * w[i][j];
			}
		}

		ll ans = -1;
		for(ll k=min(n, m); k>=3 && ans==-1; --k) {
			for(ll i=k; i<=n && ans==-1; ++i) {
				for(ll j=k; j<=m && ans==-1; ++j) {
					if(check(i, j, k)) {
						ans = k;
						//printf("%I64d %I64d %I64d\n", i, j, k);
					}
				}
			}
		}

		printf("Case #%I64d: ", q);
		if(ans == -1) puts("IMPOSSIBLE");
		else printf("%I64d\n", ans);
	}
	return 0;
}

