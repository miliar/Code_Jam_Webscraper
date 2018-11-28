#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

#define MAXN 510
#define ll long long
#define MOD 100003


ll c[MAXN][MAXN], d[MAXN][MAXN];
int n;

ll dfs(int i, int j){
	if (j == 1)return 1;
	if (d[i][j] != -1)return d[i][j];
	d[i][j] = 0;
	for (int k = 1; k < j; k++){
		d[i][j] += dfs(j, k) * c[i - j - 1][j - k - 1];
		d[i][j] %= MOD;
	}
	return d[i][j];
}

void init(){
	int i, j;
	for (i = 0; i <= 500; i++){
		c[i][0] = c[i][i] = 1;
	}
	for (i = 2; i <= 500; i++){
		for (j = 1; j < i; j++){
			c[i][j] = c[i - 1][j] + c[i - 1][j - 1];
			c[i][j] %= MOD;
		}
	}
}

int main(){
	freopen("/home/liang/桌面/C-large.in", "r", stdin);
	freopen("ans.out", "w", stdout);
	init();
	int i, j, k;
	int T, cas = 1;
	ll ans;
	scanf("%d", &T);
	while (T--){
		scanf("%d", &n);
		memset(d, -1, sizeof(d));
		ans = 0;

		for (j = 1; j < n; j++){
			ans += dfs(n, j);
			ans %= MOD;
		}
		//printf("%lld\n", ans);
		printf("Case #%d: %lld\n", cas++, ans);
	}
	return 0;
}



