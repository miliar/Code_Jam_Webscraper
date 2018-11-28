#include <cstdio>
#include <string>
#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

const int N = 512;
const int MOD = 100003;

int c[N][N], dp[N][N];

int C(int n, int k)
{
	if(k < 0 || k > n) return 0;
	if(k == 0 && k == n) return 1;
	if(c[n][k] != -1) return c[n][k];
	else return c[n][k] = (C(n-1, k)+C(n-1, k-1))%MOD;
}

int go(int k, int n)
{
	int& res = dp[k][n];
	if(res != -1) return res;
	
	if(n <= 1) return 0;
	if(k == 1) return 1;
	
	res = 0;
	
	// (k, n) -> (x, k) 
	// [k+1, n)
	for(int i = 0; i <= n-k-1; i++) {
		if(i+1 >= k) break;
		res = (res+1LL*C(n-k-1, i)*go(k-i-1, k))%MOD;
	}
	
	return res;
}

int main()
{
	memset(c, -1, sizeof(c));
	memset(dp, -1, sizeof(dp));
	
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		int res = 0;
		int n;
		scanf("%d", &n);
		for(int i = 1; i < n; i++) res = (res+go(i, n))%MOD;
		
		printf("Case #%d: %d\n", t+1, res);
	}
	
	return 0;
}

