#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

struct group
{
	double pos;
	double num;
};

vector<group> groups;
int t, c, d;

bool check(double t)
{
	double lb = -1e12;
	for(int i = 0; i < c; i++)
	{
		double lg = max(lb, groups[i].pos - t);
		double lng = (groups[i].num - 1) * d;
		if(lg + lng - groups[i].pos > t)
			return false;
		lb = lg + lng + d;
	}
	return true;
}


double solve()
{
	double l = 0.0, r = 1e12, m;
	for(int it = 0; it < 256; it++)
	{
		m = (l + r) / 2.0;
		if(check(m))
			r = m;
		else
			l = m;
	}
	return (l + r) / 2.0;
}

int main()
{
	scanf("%d", &t);
	for(int test = 0; test < t; test++)
	{
		scanf("%d%d", &c, &d);
		groups.resize(c);

		for(int i = 0; i < c; i++)
			scanf("%lf%lf", &groups[i].pos, &groups[i].num);

		printf("Case #%d: %.9lf\n", test + 1, solve());
	}
	return 0;
}