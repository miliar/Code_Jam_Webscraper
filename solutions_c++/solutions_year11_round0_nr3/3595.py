#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int nc, tc;
	int i, n;
	int mask, total, min1, bil;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		scanf("%d", &n);
		mask = 0;
		total = 0;
		for (i = 0; i < n; i++) {
			scanf("%d", &bil);
			total += bil;
			mask ^= bil;
			if (i == 0)
				min1 = bil;
			else
				min1 = min(min1, bil);
		}
		if (mask > 0)
			printf("Case #%d: NO\n", nc);
		else
			printf("Case #%d: %d\n", nc, total-min1);
	}
}
