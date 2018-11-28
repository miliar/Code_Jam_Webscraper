#include <stdio.h>

int r, k, n;
int g[1010];
int next[1010];
int value[1010];

__int64 calc(){
	int s = 0;
	int i = 0;
	int j = 0;
	for (i = 0; i < n; i++){
		while (s + g[j] <= k){
			s += g[j]; j++;
			if (j >= n) j = 0;
			if (j == i) break;
		}

		next[i] = j; 
		value[i] = s;
		s -= g[i];
	}

	int m = 0;
	__int64 ss = 0;
	i = 0;

	do {
		m++;
		ss += value[i];
		i = next[i];
		if (m >= r) break;
	} while (i != 0);

	__int64 res = ss * (__int64)(r / m);

	r %= m; i = 0;
	while (r--){
		res += value[i];
		i = next[i];
	}

	return(res);
}

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		scanf("%d%d%d", &r, &k, &n);
		for (int j = 0; j < n; j++)
			scanf("%d", &g[j]);
		printf("Case #%d: %I64d\n", i, calc());
	}
	return 0;
}
