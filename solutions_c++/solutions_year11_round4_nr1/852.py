#include <cstdio>
#include <algorithm>
using namespace std;
struct interval
{
	int speed;
	int from, to;
	bool operator < (const interval &other) const
	{
		return speed < other.speed;
	}
} I[5000];
const double EPS = 1e-9;
void solve()
{
	int X, S, R, N;
	double t;
	scanf ("%d%d%d%lf%d", &X, &S, &R, &t, &N);
	int last = 0;
	int cnt = 0;
	for (int i = 0; i < N; ++i)
	{	
		int f, t, s, w;
		scanf ("%d%d%d", &f, &t, &w);
		if (f > last)
		{
			I[cnt].from = last;
			I[cnt].to = f;
			I[cnt].speed = S;
			++cnt;
		}
		I[cnt].from = f;
		I[cnt].to = t;
		I[cnt].speed = S + w;
		++cnt;
		last = t;
	}
	if (I[cnt - 1].to < X)
	{
		I[cnt].from = last;
		I[cnt].to = X;
		I[cnt].speed = S;
		++cnt;
	}
	sort(I, I + cnt);
	double ans = 0;
	for (int i = 0; i < cnt; ++i)
	{
		double time = (I[i].to - I[i].from) / ((I[i].speed + R - S) * 1.);
		if (time < t)
		{
			t -= time;
			ans += time;
		}
		else
		{
			ans += t;
			double dist = I[i].to - I[i].from - (I[i].speed + R - S) * t;
			t = 0;
			ans += dist / I[i].speed;
		}
	}
	printf ("%.7lf\n", ans);
}	
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}