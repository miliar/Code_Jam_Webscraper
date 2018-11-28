#include <algorithm>
#include <cmath>
#include <cstdio>
using namespace std;
const int N = 1000000;
double sta[N], tmp[N];
int d, stalen;

inline bool ko(double t)
{
	sta[0] -= t;
	for (int i = 1; i < stalen; ++i)
	{
		if (sta[i] - sta[i - 1] > d)
		{
			sta[i] = max(sta[i] - t, sta[i - 1] + d);
		}
		else
		{
			sta[i] = min(sta[i] + t, sta[i - 1] + d);
		}
		if (fabs(sta[i] - sta[i - 1]) < d)
		{
			return 0;
		}
	}
	return 1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int testi = 0; testi < test; ++testi)
	{
		stalen = 0;
		int c;
		scanf("%d%d", &c, &d);
		while (c--)
		{
			int p, v;
			scanf("%d%d", &p, &v);
			while (v--)
			{
				sta[stalen++] = p;
			}
		}
		sort(sta, sta + stalen);
		memcpy(tmp, sta, sizeof(tmp));
		double left = 0, right = 200 * N;
		while (right - left > 1e-7)
		{
			memcpy(sta, tmp, sizeof(sta));
			double mid = (left + right) / 2;
			if (ko(mid))
			{
				right = mid;
			}
			else
			{
				left = mid;
			}
		}
		printf("Case #%d: %.6lf\n", testi + 1, left);
	}
	return 0;
}