#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

int t[200], s, p, n, m;

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	scanf("%d", &m);
	for (int i = 0; i < m; ++i) {
		scanf("%d%d%d", &n, &s, &p);
		for (int j = 0; j < n; ++j)
			scanf("%d", &t[j]);
		sort(t, t + n); int ans = 0;
		for (int k = 0; k < n; ++k)
			if ((t[k] + 2) / 3 >= p) ++ans;
			else if (s && t[k] && t[k] % 3 != 1 && (t[k] + 2) / 3 + 1 >= p) {
				--s; ++ans;
			}

		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}
