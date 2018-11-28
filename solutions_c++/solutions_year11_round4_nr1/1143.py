#include <cstdio>
#include <ctime>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795

int main()
{
	freopen("gcj_r2.in", "r", stdin);
	freopen("gcj_r2.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for(int it=1; it<=tc; ++it)
	{
		int x, s, r, n;
		double t;
		scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
		vector< pair<int, int> > seg;
		r-=s;
		for(int i=0; i<n; ++i)
		{
			int sl, sr, sv;
			scanf("%d%d%d", &sl, &sr, &sv);
			sv+=s;
			seg.pb(mp(sv, sr-sl));
			x-=(sr-sl);
		}
		seg.pb(mp(s, x));
		sort(seg.begin(), seg.end());
		double res=0;
		for(int i=0; i<seg.size(); ++i)
		{
			double rt=min(seg[i].sc*1.0/(seg[i].fs+r), t);
			res+=(seg[i].sc-rt*r)/seg[i].fs;
			t-=rt;
		}
		printf("Case #%d: %.10lf\n", it, res);
	}
	return 0;
}