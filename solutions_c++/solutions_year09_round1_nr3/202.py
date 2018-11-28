#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define MAXN 41

double dp[30000][MAXN];

double combine(int n, int m){
	double a = n, b = m, res = 1.0;
	if(2.0 * b >= a) b = a - b;
	while(b >= 1.0){
		res = res * a / b;
		b -= 1.0;
		a -= 1.0;
	}
	return res;
}

int main(){
	int cases, n, m;
	freopen("D:\\C-large.in", "r", stdin);
	freopen("D:\\result.out", "w", stdout);
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		scanf("%d%d", &n, &m);
		int bound = n * 200;
		for(int i = 1; i <= bound; ++i)
			for(int j = 0; j <= n; ++j) dp[i][j] = 0.0;
		dp[1][m] = 1.0;
		for(int i = 2; i <= bound; ++i)
			for(int j = m; j <= min(n, i * m); ++j){
				if(j != n)
				for(int k = max(m, j - m); k <= min(j, (i- 1) * m); ++k)
					dp[i][j] += dp[i - 1][k] * combine(n - k, j - k) * combine(k, m - (j - k))/ combine(n, m);
				else
				for(int k = max(m, j - m); k <= min(j - 1, (i - 1) * m); ++k)
					dp[i][j] += dp[i - 1][k] * combine(n - k, j - k) * combine(k, m - (j - k)) / combine(n, m);
			}
		double sum = 0.0;
		for(int i = 1; i <= bound; ++i)
			sum += (double)i * dp[i][n];
		//printf("%d %d\n", n, m);
		printf("Case #%d: %.7lf\n", case_t, sum);
//		system("pause");
	}
	return 0;
}