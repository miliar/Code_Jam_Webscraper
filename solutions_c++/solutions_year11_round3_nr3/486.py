/*
 * B.cpp
 *
 *  Created on: 2011-5-22
 *      Author: stm
 */

#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int MAXN = 100;
int a[MAXN];
int N, L, H, T;

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d%d", &N, &L, &H);
		for (int i = 0; i < N; ++i)
			scanf("%d", &a[i]);

		int ans;
		bool found;
		for (ans = L; ans <= H; ++ans) {
			found = true;
			for (int i = 0; i < N; ++i)
				if (a[i] > 0)
					if (a[i] % ans &&  ans % a[i]) {
						found = false;
						break;
					}
			if (found) break;
		}
		printf("Case #%d: ", t);
		if (!found)
			puts("NO");
		else
			printf("%d\n", ans);
	}
	return 0;
}
