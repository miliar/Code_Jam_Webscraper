#include <cstdio>
using namespace std;
char Map[110][110];
double OWP[110];
int N;
void calcOWP(int t)
{
	double ans = 0;
	int cntteams = 0;
	for (int i = 0; i < N; ++i)
	{
		if (Map[i][t] != '.')
		{
			++cntteams;
			int cnt = 0;
			int cur = 0;
			for (int j = 0; j < N; ++j)
			{
				if (Map[i][j] != '.' && j != t)
				{
					++cnt;
					if (Map[i][j] == '1') ++cur;
				}
			}
			ans += (1. * cur) / cnt;
		}
	}
	ans /= cntteams;
	OWP[t] = ans;
}
void solve()
{	
	scanf ("%d\n", &N);
	for (int i = 0; i < N; ++i)
	{
		gets(Map[i]);
	}
	for (int i = 0; i < N; ++i)
		calcOWP(i);
	for (int i = 0; i < N; ++i)
	{
		double ans = 0;
		int cnt = 0;
		double cur = 0;
		for (int j = 0; j < N; ++j)
		{
			if (Map[i][j] != '.')
			{
				++cnt;
				if (Map[i][j] == '1') ++cur;
			}
		}
		ans += (0.25 * cur) / cnt;
		ans += OWP[i] * 0.5;
		cnt = 0;
		cur = 0;
		for (int j = 0; j < N; ++j)
		{
			if (Map[i][j] != '.')
			{
				++cnt;
				cur += OWP[j];
			}
		}
		ans += 0.25 * cur / cnt;
		printf ("%.10lf\n", ans);
	}
}
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d:\n", i + 1);
		solve();
	}
	return 0;
}