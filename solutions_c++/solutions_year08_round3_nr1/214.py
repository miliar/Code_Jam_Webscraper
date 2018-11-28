#include <iostream>
#include <cstdio>
#include <algorithm>
#include <functional>
#include <vector>
using namespace std;

int a[1024];

int main()
{
	int n, k, l;

	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	scanf("%d", &n);
	for (int cas = 1; cas <= n; ++cas) {
		scanf("%*d %d %d", &k, &l);
		for (int i = 0; i < l; ++i)
			scanf("%d", &a[i]);
		sort(a,a+l, greater<int>());
		int res = 0, t = 1;
		for (int i = 0; i < l; i += k) {
			for (int j = 0; j < k && i + j < l; ++j)
				res += a[i + j] * t;
			++t;
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}

