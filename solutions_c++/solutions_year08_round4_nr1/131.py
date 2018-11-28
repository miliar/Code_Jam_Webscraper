#include <cstdio>

int m;
int g[16384];
int c[16384];
int t[16384][2];

int min(int a, int b){
	return a>b?b:a;
}

int isint(int k){
	return k*2 < m;
}

int dp(int k, int v){
	if (!isint(k))
		return g[k]==v?0:16384;
	if (t[k][v] != -1)
		return t[k][v];
	int result;
	if (g[k]){
		if (v)
			result = dp(k*2, 1) + dp(k*2+1, 1);
		else
			result = min(dp(k*2,0), dp(k*2+1,0));
	} else {
		if (v)
			result = min(dp(k*2,1), dp(k*2+1,1));
		else
			result = dp(k*2, 0) + dp(k*2+1, 0);
	}
	if (c[k]){
		if (!g[k]){
			if (v)
				result = min(result,dp(k*2, 1) + dp(k*2+1, 1)+1);
			else
				result = min(result,min(dp(k*2,0), dp(k*2+1,0))+1);
		} else {
			if (v)
				result = min(result,min(dp(k*2,1), dp(k*2+1,1))+1);
			else
				result = min(result,dp(k*2, 0) + dp(k*2+1, 0)+1);
		}
	}
	return t[k][v] = result;
}

int main(){
	int n;
	scanf("%d", &n);

	for (int cases = 0; cases < n; cases++){
		int v;
		scanf("%d%d", &m, &v);

		for (int tmp = 1; tmp <= m; tmp++){
			if (isint(tmp))
				scanf("%d%d", &g[tmp], &c[tmp]);
			else
				scanf("%d", &g[tmp]);
			t[tmp][0] = t[tmp][1] = -1;
		}
		int result = dp(1, v);
		if (result > 11000)
			printf ("Case #%d: IMPOSSIBLE\n", cases+1);
		else
			printf ("Case #%d: %d\n", cases+1, result);
	}
	return 0;
}
