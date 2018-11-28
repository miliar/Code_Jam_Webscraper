/*
 * a.cpp
 *
 *  Created on: Jun 4, 2011
 *      Author: ahmed
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;

int main()
{

	freopen("A-large.in", "rt", stdin);
	freopen("b.txt", "wt", stdout);

	int t;scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		printf("Case #%d: ", ii+1);
		int x, s, r, t, n;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		vector<pair<int, int > >vp;
		int all = 0;
		for (int i = 0; i < n; ++i) {
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);
			vp.pb(mp(s+w, abs(e-b)));
			all+=abs(e-b);
		}
		double rem = (double)x - (double)all;
		int dst = t*r;
		double res = 0.0, tm = (double )t;
		if((double)dst - rem >= 1e-9)
			res += rem / (double)r, tm-=res, rem = 0.0;
		else
			res += (double)dst / (double)r, tm = 0, rem -= dst;
		res+= rem/(double)s;
		sort(vp.begin(), vp.end());
		for (int i = 0; i < (int )vp.size(); ++i) {
			if(tm - 0 >= 1e-9 ) {
				double speed = (r + vp[i].first - s);
				double d = tm * speed;
				double curD = (double)vp[i].second;
				if(d - curD >= 1e-9)
					res += curD / speed, tm-=curD/speed, curD = 0.0;
				else
					res += d/speed, tm = 0, curD-=d;
				res+= curD / (double)vp[i].first;
			}
			else {
				res+=(double)vp[i].second/(double)vp[i].first;
			}
		}
		printf("%.9f\n", res);
	}
	return 0;
}

/*
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
