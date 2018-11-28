#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int MOD = 100003;
int c[512][512];
int f[512][512];

int solve(int n, int k){
	if (f[n][k] != -1)
		return f[n][k];
	int res = 0;
	
	for (int l=1; l<k; ++l){
		if ((k-l-1 <= n-k-1) && (l-1 <= k-2)){
			res = (res + solve(k, l)*c[n-k-1][k-l-1]) % MOD;
		}	
	}	
	
	f[n][k] = res;
	return res;
}

int main(){	
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	for (int i=0; i<512; ++i)
		c[i][0] = 1;
		
	for (int i=1; i<512; ++i)
		for (int j=1; j<=i; ++j)
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % MOD;
			
	memset(f, 0xff, sizeof(f));
	for (int i=2; i<512; ++i)
		f[i][1] = 1;
	
	int ntest;
	
	scanf("%d", &ntest);
	
	for (int itest=0; itest<ntest; ++itest){
	
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", itest+1);
		
		int ans = 0;
		for (int i=1; i<n; ++i)
			ans = (ans + solve(n, i)) % MOD;

		printf("%d\n", ans % MOD);	
	}

    return 0;
}

