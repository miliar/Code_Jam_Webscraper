#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

const int maxn = 201;
int a[maxn], p, S, n;

bool cmp(int x, int y)
{
	return x > y;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int TextN, TT = 0;
	scanf("%d", &TextN);
	while (TextN--) {
		scanf("%d%d%d", &n, &S, &p);
		for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
		sort(a+1, a+1+n, cmp);
		int Ans = 0;
		for (int i = 1; i <= n; i++) {
			if (a[i] >= max(p, 3*p-2)) ++Ans;
			else {
				if (a[i] >= max(p, 3*p-4) && S>0) {
					++Ans;
					--S;
				}
			}
		}
		printf("Case #%d: %d\n", ++TT, Ans);
	}
	return 0;
}