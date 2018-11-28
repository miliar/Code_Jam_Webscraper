#include <algorithm>
#include <cstdio>
using namespace std;
typedef pair<int, int> PII;
PII pii[2222];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int testi = 0; testi < test; ++testi)
	{
		int x, s, r, tt, n;
		int sum = 0;
		scanf("%d%d%d%d%d", &x, &s, &r, &tt, &n);
		double t = tt;
		for (int i = 0; i < n; ++i)
		{
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);
			sum += e - b;
			pii[i] = PII(w, e - b);
		}
		pii[n++] = PII(0, x - sum);
		sort(pii, pii + n);
		double ans = 0;
		for (int i = 0; i < n; ++i)
		{
			double tt = 1.0 * pii[i].second / (r + pii[i].first);
			if (tt < t)
			{
				ans += tt;
				t -= tt;
			}
			else
			{
				ans += t;
				ans += 1.0 * (pii[i].second - t * (r + pii[i].first)) / (s + pii[i].first);
				t = 0;
			}
		}
		printf("Case #%d: %.9lf\n", testi + 1, ans);
	}
	return 0;
}