#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

struct Way {
	int s, t, w, len;
};

bool operator < (const Way & A, const Way & B)
{
	return A.w < B.w;
}

int		n;
double	tim;
int		S, R;
int		X;
Way		list	[1000 + 100];

void init()
{
	scanf("%d%d%d%lf%d", &X, &S, &R, &tim, &n);
	double len = X;
	for (int i = 0; i < n; i ++)
	{
		scanf("%d%d%d", &list[i].s, &list[i].t, &list[i].w);
		list[i].len = list[i].t - list[i].s;
		len -= list[i].len;
	}
	list[n].w = 0;
	list[n].len = len;
	n ++;
}

void solve()
{
	double ret = 0;
	sort(list, list + n);
	for (int i = 0; i < n; i ++)
	{
		double t = (double)list[i].len / (R + list[i].w);
		if (t <= tim)
		{
			tim -= t;
			ret += t;
		}
		else
		{
			double left = list[i].len - (R + list[i].w) * tim;
			ret += tim;
			tim = 0;
			ret += left / (S + list[i].w);
		}
	}

	printf("%.10lf\n", ret);
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//freopen("in.txt", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t ++)
	{
		init();
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
