/*
 * C.cpp
 *
 *  Created on: 2011-5-7
 *      Author: stm
 */

#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 110;
int n, p[MAXN], ans, T, a[MAXN];

void Check()
{
	int s1 = 0, s2 = 0, sum = 0, sum2 = 0;
	for (int i = 0; i < n; ++i) {
		if (p[i] == 0) {
			s1 ^= a[i];
			sum += a[i];
		}
		else {
			s2 ^= a[i];
			sum2 += a[i];
		}
	}
	if (s1 == s2 && sum > 0 && sum2 > 0) {
		if (sum > ans)
			ans = sum;
	}
}

void Search(int k)
{
	if (k >= n) {
		Check();
		return;
	}
	for (int i = 0; i < 2; ++i) {
		p[k] = i;
		Search(k + 1);
	}
}

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		ans = -1;
		Search(0);
		printf("Case #%d: ", t);
		if (ans == -1) puts("NO");
		else printf("%d\n", ans);
	}
	return 0;
}
