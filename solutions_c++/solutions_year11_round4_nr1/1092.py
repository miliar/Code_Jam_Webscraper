#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <memory>
#include <cctype>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;  
#ifdef LOCAL_MASHINE
typedef __int64 long long;
#endif
typedef long long INT64;
#define min(a,b) ((a)<(b)?a:b)
#define max(a,b) ((a)>(b)?a:b)
#define sz(a) int((a).size())
#define INF 2000000000

int t,T;
int wsp, rs, rtm, x, n;
double rt;
int i;
int l;
int g,h,f;
double res, tm;

pair<int, int> a[1000005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for (t=1; t<=T; t++)
	{
		scanf("%d%d%d%d%d",&x, &wsp, &rs, &rtm, &n);
		rt = rtm;
		if (rs <= wsp)
		{
			rt = 0;
		}
		l = 0;
		res = 0;
		for(i=0; i<n; i++)
		{
			scanf("%d%d%d", &g, &h, &f);
			a[i].first=f;
			a[i].second = h-g;
			l += h-g;
		}
		a[n].first = 0;
		a[n].second = x-l;
		sort(a, a+n+1);
		for (i=0; i<=n; i++)
		{
			if (rt>0)
			{
				tm = a[i].second/(double)(a[i].first+rs);
				if (rt>tm)
				{
					rt-=tm;
					res+=tm;
				}
				else
				{
					
					res+=rt;
					res+=(a[i].second - rt*(a[i].first+rs))/(double)(a[i].first+wsp);
					rt = 0;
				}
			}
			else
			{
				res+=a[i].second/(double)(a[i].first+wsp);
			}
		}
		printf("Case #%d: %.9lf\n", t, res);
	}

	return 0;
}

/*
1
10 1 100 1 2
4 6 1
6 9 2

3
10 1 4 1 2
4 6 1
6 9 2
12 1 2 4 1
6 12 1
20 1 3 20 5
0 4 5
4 8 4
8 12 3
12 16 2
16 20 1
*/
