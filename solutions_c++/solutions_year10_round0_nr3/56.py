/*
 * C.cpp
 *
 *  Created on: 2010-5-8
 *      Author: aaahexing
 */

#include <set>
#include <map>
#include <cctype>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

long long s[1001], dp[1001];
int cas, R, k, N, g[1001], pr[1001], r[1001];

inline long long gao() {
	int p = -1, q = -1, st = 0;
	long long ret = 0;

	for (int i = 0; i < N; i ++) {
		r[i] = -1;
		dp[i] = 0;
		s[i] = g[i];
		pr[i] = (i+1) % N;
//		printf("i = %d, pr[i] = %d\n", i, pr[i]);
		for (int j = (i+1)%N; j != i && s[i]+g[j] <= k; j = (j+1)%N) {
			s[i] += g[j];
			pr[i] = (j+1) % N;
//			printf("i = %d, pr[i] = %d\n", i, pr[i]);
		}
	}
//	for (int i = 0; i < N; i ++) {
//		printf("%lld(%d) ", s[i], pr[i]);
//	}
//	puts("");

	st = 0;
	for (int i = 0; ; i ++) {
//		printf("st = %d\n", st);
		if (r[st] != -1) {
			p = r[st];
			q = i - r[st];
//			printf("p = %d, q = %d\n", p, q);
			break;
		}
		r[st] = i;
		dp[i] += s[st];
		st = pr[st];
	}

	long long s1 = 0;
	long long s2 = 0;
	for (int i = 0; i < p; i ++) {
		s1 += dp[i];
//		printf("%d ", dp[i]);
	}
//	puts("");
	for (int i = p; i < p+q; i ++) {
		s2 += dp[i];
//		printf("%d ", dp[i]);
	}
//	puts("");

	if (R <= p) {
		ret = 0;
		for (int i = 0; i < R; i ++)
			ret += dp[i];
	}
	else {
		ret = s1;
		ret += ((R-p)/q) * s2;
//		printf("ret = %lld\n", ret);
		for (int i = 0; i < (R-p)%q; i ++)
			ret += dp[p+i];
	}

	return ret;
}

int main() {
	freopen("C-small.in", "r", stdin); freopen("C-small.out", "w", stdout);
//	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);

	scanf("%d", &cas);
	for (int c = 1; c <= cas; c ++) {
		scanf("%d%d%d", &R, &k, &N);
		for (int i = 0; i < N; i ++)
			scanf("%d", &g[i]);
		printf("Case #%d: %lld\n", c, gao());
	}

	return 0;
}
