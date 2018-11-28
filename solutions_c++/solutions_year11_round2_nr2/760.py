#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <memory>
#include <string>
#include <set>
#include <map>
#include <queue>
using namespace std;
	vector<double> vv;
double d;
int check(double t)
{
	double st = vv[0]-t;
	st += d;
	double eps = 1e-12;
	for (int i = 1; i < vv.size(); i++)
	{
		if ((fabs(vv[i]-st) - t) <=eps)
			st += d; else
		{
			if ((vv[i] - t) > st )
			{
				st = vv[i]-t + d;
			} else
				if ((vv[i] + t) < st)
					return 0;
		}
	}
	return 1;
}
int main(void)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,q;
	scanf("%d",&t);

	for (q = 1; q <= t; q++)
	{
		int c,v;
		double p;
		vv.clear();
		scanf("%d%lf",&c,&d);
		for (int i = 0; i < c; i++)
		{
			scanf("%lf%d",&p,&v);
			for (int i = 0; i < v; i++)
				vv.push_back(p);
		}
		sort(vv.begin(),vv.end());
		double s,f,m;
		s = 0;
		f = 1000000000000.0;
		double eps = 1e-12;
		while (fabs(f-s) > eps)
		{
			m = (s + f) / 2;
			if (check(m))
				f = m; else
				s = m;
		}
		if (check(s))
			printf("Case #%d: %.6lf\n",q,s); else
			printf("Case #%d: %.6lf\n",q,f);
	}
	return 0;
}