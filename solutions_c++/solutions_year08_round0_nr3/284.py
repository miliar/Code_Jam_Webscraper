#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cctype>
#include <memory>
#include <vector>
#include <list>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;


typedef long long Int;
typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef pair<int,int> PII;


#define FOR(i,n,m) for(i=(n); i<(m); ++i)
#define RFOR(i,n,m) for(i=(n)-1; i>=(m); --i)
#define CLEAR(x,y) memset((x), (y), sizeof(x))
#define COPY(x,y) memcpy((x),(y),sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, ts;
	scanf("%d", &T);
	for (ts = 0; ts < T; ++ts)
	{
		double f, R, t, r, g;
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		fprintf(stderr, "%d\n", ts+1);
		double all = R*R*2*acos(0.0);
		double s = 0;
		R -= t;
		R -= f;
		r += f;
		g -= f+f;
		if (R <= 0 || g <= 0)
			s = 0;
		else
		{
			double ay, by;
			for (ay = r; ay < R; ay += g+r+r)
			{
				by = ay + g;
				double ax, bx;
				double ex = sqrt(R*R - ay*ay);
				for (ax = r; ax < ex; ax += g+r+r)
				{
					bx = ax + g;
					if (bx > ex)
						bx = ex;
					s += (R*R*atan2(bx, sqrt(R*R-bx*bx))+bx*sqrt(R*R-bx*bx) - R*R*atan2(ax, sqrt(R*R-ax*ax))-ax*sqrt(R*R-ax*ax) - ay*(bx-ax)*2.0 )*2.0;
				}
				if (by < R)
				{
					ex = sqrt(R*R - by*by);
					for (ax = r; ax <= ex; ax += g+r+r)
					{
						bx = ax + g;
						if (bx > ex)
							bx = ex;
						s -= (R*R*atan2(bx, sqrt(R*R-bx*bx))+bx*sqrt(R*R-bx*bx) - R*R*atan2(ax, sqrt(R*R-ax*ax))-ax*sqrt(R*R-ax*ax) - by*(bx-ax)*2.0 )*2.0;
					}
				}
			}
		}
		double res = 1 - s / all;
		printf("Case #%d: %.10lf\n", ts+1, res);
	}
	return 0;
}