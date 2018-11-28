#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<sstream>
#include<queue>
#include<string>
#include<cmath>

using namespace std;

#define pb push_back
#define re return
#define sf scanf
#define pf printf

int dp[505][505];
const int mod = 100003;
int ncr[505][505];

void gen_ncr() {
	int i, j;
	for(i=0;i<=500;i++)
	  ncr[i][0] = 1;

	for(i=1;i<=500;i++)
	 for(j=1;j<=i;j++) {
	   ncr[i][j] = ncr[i-1][j-1] + ncr[i-1][j];
	   ncr[i][j] %= mod;
	 }
}

int memo(int n, int k) {
	int i;
	if( k == 1 ) return 1;
	if( dp[n][k] != -1 ) return dp[n][k];
	int res = 0;
	for(i=1;i<k;i++) {
		int m = memo(k, i);
		m %= mod;
		int r = ncr[n-k-1][k-i-1];
		long long L = m;
		L = L * r; L %= mod;
		res += L;
	}
	return dp[n][k] = res;
}

int main() {
	int t;
	int cases = 1;
	gen_ncr();
	int i, j;
	for(i=0;i<=502;i++)
	 for(j=0;j<=502;j++)
	  dp[i][j] = -1;
	for( sf("%d", &t); t--;) {
		int n;
		cin >> n;

		int res = 0;
		for(i=1;i<n;i++) {
		  res += memo(n, i);
		  res %= mod;
		}

		pf("Case #%d: %d\n", cases++, res);
	}

	return 0;
}
