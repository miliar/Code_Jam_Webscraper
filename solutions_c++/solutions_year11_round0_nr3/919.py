#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int numCase = 1; numCase <= T; ++numCase) {
		int n;
		scanf("%d", &n);
		int mn = ~0U >> 1;
		int sum = 0, tot = 0;
		for (int i = 0; i < n; ++i) {
			int x;
			scanf("%d", &x);
			mn = min(mn, x);
			sum ^= x;
			tot += x;
		}
		printf("Case #%d: ", numCase);
		if (sum != 0) puts("NO");
		else printf("%d\n", tot - mn);
	}
}
