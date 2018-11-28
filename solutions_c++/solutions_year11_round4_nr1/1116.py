#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <algorithm>
#include <cassert>
#include <memory.h>
#include <sstream>
#include <iostream>

using namespace std;

#define mp make_pair
#define pb push_back

void prepare()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

int n;
double t;
double s, r, x;
pair< double, pair<double, double> > ways[1005];

void solve()
{
	scanf("%lf%lf%lf", &x, &s, &r);
	scanf("%lf", &t);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%lf%lf%lf", &ways[i].second.first, &ways[i].second.second, &ways[i].first);

	sort(ways, ways + n);
	reverse(ways, ways + n);

	double sumlen = 0.0;
	for (int i = 0; i < n; i++)
		sumlen += ways[i].second.second - ways[i].second.first;

	double left = x - sumlen;
	ways[n++] = mp( 0.0, mp(0, left) );
	reverse(ways, ways + n);

	double ans = 0.0;
	for (int i = 0; i < n; i++)
	{
		double len = ways[i].second.second - ways[i].second.first;
		double need = len / (r + ways[i].first);
		if (t >= need)
		{
			ans += need;
			t -= need;
		}
		else
		{
			ans += t + (len - (r + ways[i].first) * t) / (s + ways[i].first);
			t = 0;
		}
	}

	static int TEST = 0;
	printf("Case #%d: %.6lf\n", ++TEST, ans);
}

int main()
{
	prepare();
	int tn;
	for (scanf("%d", &tn); tn; tn--)
		solve();
	return 0;
}