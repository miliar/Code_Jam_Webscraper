#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cctype>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define maxn 1100

pair<int, int> c[maxn];
int n, x, s, t, r;

int main()
{
#ifdef impetus
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int testnum;
	scanf("%d", &testnum);
	for (int tc = 0; tc < testnum; tc++)
	{
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			int p, q;
			scanf("%d%d%d", &p, &q, &c[i].first);
			c[i].second = q - p;
			c[i].first += s;
			sum += c[i].second;
		}
		c[n].second = x - sum;
		c[n].first = s;
		sort(c, c + n + 1);
		r -= s;
		double time = 0;
		double z = 0;
		for (int i = 0; i <= n; i++)
		{
			double left = 0;
			if (z + 1e-8 < t)
			{
				if ((t - z) * (c[i].first + r) < c[i].second)
				{
					left = c[i].second - (t - z) * (c[i].first + r);
					time += t - z;
					z = t;
				}
				else
				{
					left = 0;
					time += 1.0 * c[i].second / (c[i].first + r);
					z += 1.0 * c[i].second / (c[i].first + r);
				}
			}
			else
				left = c[i].second;
			time += left / c[i].first;
		}
		printf("Case #%d: %0.9lf\n", tc + 1, time);
	}
	return 0;
}