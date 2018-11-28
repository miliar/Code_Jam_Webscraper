#include <stdio.h>
#include <algorithm>

using namespace std;


void solve()
{
	int n, m, a;
	scanf("%d%d%d", &n, &m, &a);
	if (a <= 2 * n * m)
		for (int x1 = 0; x1 <= n; ++x1)
			for (int x2 = 0; x2 <= n; ++x2)
				for (int y2 = 0; y2 <= m; ++y2) 
					if (x2 == 0 && a == x1 * y2 || x2 != 0 && (x1 * y2 - a) % x2 == 0){
						int y1 = x2 ? (x1 * y2 - a) / x2 : 1;
						if (y1 >= 0 && y1 <= m) {
							if (a != x1*y2 - y1*x2) throw 0;
							printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
							return;
						}
					}
	printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n; scanf("%d", &n); 
	for (int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
}