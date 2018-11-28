#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define all(x) ((x).begin, (x).end)
#define eps	1e-15

typedef long long int lint;

double solve()
{
	int t, x, n, r, s;

	scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);

	vector<pair<int, int> > v;
	v.reserve(n + 1);
	int walk = x;
	REP(i,n) {
		int b, e, d;
		scanf("%d%d%d",&b,&e,&d);
		walk -= ( e - b );
		v.push_back(make_pair(d, (e-b)));
	}
	v.push_back(make_pair(0, walk));
	sort(v.begin(), v.end());
	double result = 0.0;
	double tt = t;
	REP(i,n+1) {
		double d = v[i].first;
		double l = v[i].second;
		double rr = d + r;
		double ss = d + s;

		if ( tt * rr < l ) {
			l -= tt * rr;
			result += tt + ( l / ss );
			tt = 0;
		}
		else {
			tt -= l / rr;
			result += l / rr;
		}
	}

	return result;
}

int main(void)
{
	int T;
	scanf("%d",&T);

	REP(i,T) {
		printf("Case #%d: ", i+1 );
		printf("%.8lf\n",solve());
	}

	return 0;
}

