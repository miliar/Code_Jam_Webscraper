#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORN(i,a,n) for (int i = (a); i < (a)+(n); ++i)

//#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
//#define SIZE(x) int(x.size())

typedef long long ll;
typedef pair<ll,ll> PLL;

/////////////////////////////////////////////////////////////////////////

vector<PLL> vendors;
ll C, D;

bool candoit(double dist)
{
	double rend = -10e14, lend;

	FOR (i, 0, C) {
		lend = max(rend+D, vendors[i].first-dist);
		rend = lend + (vendors[i].second-1)*D;
		if (rend - vendors[i].first > dist) return false;
	}

	return true;
}

void Solve(int testcase)
{
	scanf(" %lld %lld", &C, &D);

	ll V = 0, maxv = 0;
	vendors.clear();
	FOR (i, 0, C) {
		ll p, v;
		scanf(" %lld %lld", &p, &v);
		vendors.push_back(PLL(p,v));
		V += v;
		maxv = max(maxv, v-1);
	}

	double dmin = (double)(maxv*D)/2.0, dmax = V*D;

	while (dmax-dmin > 10e-7) {
		double med = (dmin+dmax)/2;
		if (candoit(med)) dmax = med;
		else dmin = med;
	}

	printf("Case #%d: ", testcase+1);
	printf("%.16f\n", dmax);
}

int main()
{
	int T;
	scanf(" %d", &T);
	FOR (t, 0, T)
		Solve(t);
	
	return 0;
}
