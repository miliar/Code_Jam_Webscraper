/*
 * A.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: Jun 5, 2010
 */

#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<utility>
#include <functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)
#define repa(v)				lpi(i, 0, sz(v)) lpi(j, 0, sz(v[i]))
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
#define pb					push_back
#define MP					make_pair

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef long double ld;

const int OO = (int) 1e8; //Small -> WRONG, Large -> OVERFLOW

const double PI = acos(-1.0);
const double EPS = (1e-7);

int dcmp(double x, double y) {
	return fabs(x - y) <= EPS ? 0 : x < y ? -1 : 1;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("csmall.txt", "wt", stdout);
#endif

	int cases;
	scanf("%d", &cases);

	lp(cc, cases) {
		int r;
		scanf("%d", &r);
		set<pair<int, int> > s1;
		int days = 0;

		lp(k, r) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			lpi(x, x1, x2+1)
				lpi(y, y1, y2+1)
					s1.insert(make_pair(x, y));
		}

		while (sz(s1)) {
			set<pair<int, int> > s2;

			vector<pair<int, int> > v(all(s1));
			pair<int, int> p1;
			rep(i, v) {
				p1 = v[i], p1.first--;
				int alive = 0;
				if (s1.count(p1))
					alive++;
				p1 = v[i], p1.second--;
				if (!alive && s1.count(p1))
					alive++;
				if(alive)
					s2.insert(v[i]);

				p1 = v[i], p1.first++, p1.second--;
				if (s1.count(p1) == 0)
					continue;
				p1 = v[i], p1.first++;
				s2.insert(p1);
			}
			s1 = s2;
			days++;
		}

		printf("Case #%d: %d\n", cc+1, days);

	}

	return 0;
}
