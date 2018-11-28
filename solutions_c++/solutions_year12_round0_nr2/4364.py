#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 111;

int a[MAXN];

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int n, s, p;
	for (int t = 1; t <= T; ++t)
	{
		scanf("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int ans = 0;
		for (int i = n - 1; i >= 0; --i)
		{
			int score = a[i] / 3;
			int r = a[i] % 3;
			if (r) ++score;
			if (score >= p) ++ans;
			else if (s)
			{
				if (score == 0 || r == 1) 
					continue;
				if (++score >= p) {
					++ans;
					--s;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	
	return 0;
}
