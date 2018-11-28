#include<cstdio>
#include<cstring>
#define MOD 100003

int DP[1000][1000];

inline int F(int n, int m){
	if (!n) return 1;
	if (n < 0) return 0;
	if (!m) return 0;
	if (DP[n][m] != -1) return DP[n][m];
	int res = 0;
	for (int i = n-1; i >= n-m; --i)
		res = (res + F(i, m)) % MOD;
	return DP[n][m] = res;
}

int main(){
	int T, ca=0;
	scanf("%d", &T);
	memset(DP, -1, sizeof(DP));
	int A[510];
	for (int i = 2; i <= 500; ++i){
		A[i] = 0;
		for (int j = 0, k= i-1 ; j <= i ; ++j, --k)
			A[i] = (A[i] + F(k, j)) % MOD;
	}
	while (T--){
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", ++ca, A[n] % MOD);
	}
	return 0;
}
