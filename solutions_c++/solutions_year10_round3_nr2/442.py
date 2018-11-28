#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<vector>

using namespace std;

#define re return
#define sf scanf
#define pf printf
#define pb push_back

int inf = 1000000000;

int dp[1005][1005];
int L, P, C;

int memo(int pare, int parena) {
	if( pare * C >= parena ) return 0;
	if( dp[pare][parena] != -1 ) return dp[pare][parena];

	int res = inf, i;

	for(i=pare*C;i<parena;i++) {
		int m = 1 + memo(i, parena);
		int n = 1 + memo(pare, i);
		if( m < n ) m = n;
		if( res > m ) res = m;
		if( i * C >= parena ) break;
	}
	dp[pare][parena] = res;
	return res;
}

int main() {
	int t, cases = 1, i, j;
	sf("%d", &t);
	while(t--) {
		cin >> L >> P >> C;
		for(i=0;i<=1000;i++)
		 for(j=0;j<=1000;j++)
		  dp[i][j] = -1;

		int res = memo(L, P);
		pf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}
