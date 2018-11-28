#include <cstdio>
#include <algorithm>
using namespace std;

pair<int, int> p[300], p2[300];
int test;
void work()
{
	int T, na, nb;
	scanf("%d%d%d", &T, &na, &nb);
	int h1, m1, h2, m2;
	for (int i = 0; i < na; ++i)
	{
		scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
		p[i].first = h1 * 60 + m1;
		p[i].second = h2 * 60 + m2 + T;
	}
	sort(p, p + na);
	for (int i = 0; i < nb; ++i)
	{
		scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
		p2[i].first = h1 * 60 + m1;
		p2[i].second = h2 * 60 + m2 + T;
	}
	sort(p2, p2 + nb);
	int sa = na, sb = nb;
	int use[300] = {};
	for (int i = 0; i < na; ++i)
	{
		for (int j = 0; j < nb; ++j)
		{
			if (!use[j] && p2[j].first >= p[i].second)
			{
				use[j] = 1;
				--sb;
				break;
			}
		}
	}
	int use2[300] = {};
	for (int i = 0; i < nb; ++i)
	{
		for (int j = 0; j < na; ++j)
		{
			if (!use2[j] && p[j].first >= p2[i].second)
			{
				use2[j] = 1;
				--sa;
				break;
			}
		}
	}
	printf("Case #%d: %d %d\n", ++test, sa, sb);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
