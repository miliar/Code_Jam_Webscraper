#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double w[1000010];
int main()
{
//	freopen("C:\\Users\\hayk\\Documents\\GCJ\\A-small-attempt1.in", "r", stdin);
//	freopen("C:\\Users\\hayk\\Documents\\GCJ\\A-small-attempt1.out", "w", stdout);
	freopen("C:\\Users\\hayk\\Documents\\GCJ\\A-large.in", "r", stdin);
	freopen("C:\\Users\\hayk\\Documents\\GCJ\\A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int nt = 1; nt <= T; ++nt)
	{
		int x, s, r, n, i;
		double t;
		scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);

		for (int i = 0; i < x; ++i)
			w[i] = 0.0;
		for (int i = 0; i < n; ++i)
		{
			int a, b, W;
			scanf("%d%d%d", &a, &b, &W);
			for (int j = a; j < b; ++j)
				w[j] = W;
		}
		for (int i = 0; i < x; ++i)
			w[i] += s;

		r -= s;
		sort(w, w + x);

		double ans = 0.0;
		for (i = 0; i < x; ++i)
		{
			if (t < -0.5)
			{
				ans += 1.0 / w[i];
				continue;
			}
			if (t * (w[i] + r) >= 1.0)
			{
				ans += 1.0 / (w[i] + r);
				t -= 1.0 / (w[i] + r);
			}
			else
			{
				ans += t + (1.0 - (w[i] + r) * t) / w[i];
				t = -1.0;
			}
		}
		printf("Case #%d: %.12lf\n", nt, ans);
	}
	return 0;
}
