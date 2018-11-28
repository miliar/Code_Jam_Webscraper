#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

struct Plant
{
	double x;
	double y;
	double r;
};

int n;
vector<Plant> plant;

vector<Plant> group1;
vector<Plant> group2;

Plant minidisc(vector<Plant> &group)
{
	Plant a;
	a.x = 0;
	a.y = 0;
	a.r = 0;

	if (group.size() == 1)
	{
		a.x = group[0].x;
		a.y = group[0].y;
		a.r = group[0].r;
	}
	else if (group.size() == 2)
	{
		double dx = group[1].x - group[0].x;
		double dy = group[1].y - group[0].y;
		double dd = sqrt(dx*dx + dy*dy);

		double sin = dy/dd;
		double cos = dx/dd;

		a.x = group[0].x - group[0].r*cos + group[1].x + group[1].r*cos;
		a.y = group[0].y - group[0].r*sin + group[1].y + group[1].r*sin;
		a.r = dd + group[0].r + group[1].r;

		a.x /= 2.0;
		a.y /= 2.0;
		a.r /= 2.0;
	}

	return a;
}

double solve(void)
{
	double result = -1;
	if (n == 0)
	{
		return 0.0;
	}

	int fn = 1 << n;

	for (int i = 1 ; i < fn ; ++i)
	{
		group1.clear();
		group2.clear();
		for (int j = 0 ; j < n ; ++j)
		{
			if (i&(1 << (j - 1)))
			{
				group1.push_back(plant[j]);
			}
			else
			{
				group2.push_back(plant[j]);
			}
		}
		if (group1.size() == 3 || group2.size() == 3) continue;

		double r = max(minidisc(group1).r, minidisc(group2).r);
		if (result == -1 || result > r)
		{
			result = r;
		}
	}

	return result;
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		plant.clear();

		scanf("%d ", &n);
		Plant p;
		for (int i = 0 ; i < n ; ++i)
		{
			scanf("%lf %lf %lf ", &p.x, &p.y, &p.r);
			plant.push_back(p);
		}

		printf("Case #%d: %.6lf\n", t, solve());
	}
}
