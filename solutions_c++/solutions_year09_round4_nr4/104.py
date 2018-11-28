#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))
#define FOR(a,b,c) for(int a=(b); a<(c); ++a)

struct Plant
{
	int x, y, r;
};

double f1(vector< Plant > &p)
{
	if (p.size() > 3) return -1;

	if (p.size() == 1) return p[0].r;
	if (p.size() == 2) return max(p[0].r, p[1].r);

	double res = 1e100;
	FOR(i,0,p.size()) FOR(j,i+1,p.size())
	{
		int d2 = sqr(p[i].x - p[j].x) + sqr(p[i].y - p[j].y);
		double len = 0.5 * (sqrt((double)d2) + p[i].r + p[j].r);
		len = max(len, (double)p[0+1+2^i^j].r);
		res = min(res, len);
	}
	return res;
}

int main()
{
    int T;

	scanf("%d", &T);
	FOR(cas,1,T+1)
	{
		int n;
		scanf("%d", &n);
		vector< Plant > p(n);
		FOR(i,0,n)
			scanf("%d%d%d", &p[i].x, &p[i].y, &p[i].r);

		printf("Case #%d: %.10lf\n", cas, f1(p));
	}	

    return 0;
}

	