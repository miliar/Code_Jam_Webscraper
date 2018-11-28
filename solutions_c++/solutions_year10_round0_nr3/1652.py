/*
 * C.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: May 8, 2010
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

vector<ll> g;
vector<ll> pos;
int R, N, K;

ll solve() {
	pos.clear();
	pos.resize(N, -1);

	int idx = 0;
	ll profitSoFar = 0;

	ll r = 0;
	vector<ll> accumP;
	vector<ll> accumR;
	ll preCycleP = 0;
	ll cycleP = 0;

	ll preCycleR = 0;
	ll cycleR = 0;

	while (r < R) {
		if (pos[idx] != -1) {
			preCycleP = (pos[idx] - 1 >= 0 ? accumP[pos[idx] - 1] : 0);
			cycleP = profitSoFar - preCycleP;
			preCycleR = (pos[idx] - 1 >= 0 ? accumR[pos[idx] - 1] : 0);
			cycleR = r - preCycleR;
			break;
		} else {
			int t = idx;
			ll cur = 0;
			while (cur + g[t] <= K) {
				cur += g[t];
				t = (t + 1) % N;
				if (t == idx)
					break;
			}
			pos[idx] = sz(accumP), idx = t;
			if (sz(accumP)) {
				accumP.push_back(accumP.back() + cur);
				accumR.push_back(accumR.back() + 1);
			} else {
				accumP.push_back(cur);
				accumR.push_back(1);
			}
			profitSoFar += cur;
		}

		r++;
	}

	if (r == R)
		return profitSoFar;

	R -= r;
	ll t = R / cycleR;
	profitSoFar += t * cycleP;
	R -= t*cycleR;

	//handle post cycle
	if (R) {
		lp(kk, R) {
			int t = idx;
			ll cur = 0;
			while (cur + g[t] <= K) {
				cur += g[t];
				t = (t + 1) % N;
				if (t == idx)
					break;
			}
			profitSoFar += cur, idx = t;
		}
	}

	return profitSoFar;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("C-large.in", "rt", stdin);
	freopen("clarge.txt", "wt", stdout);
#endif

	int cases;
	scanf("%d", &cases);
	lp(cc, cases) {
		scanf("%d%d%d", &R, &K, &N);
		g.clear();
		g.resize(N);
		rep(i, g) {
			int t;
			scanf("%d", &t);
			g[i] = t;
		}
		ll s = solve();
		cout << "Case #" << cc + 1 << ": " << s << "\n";
	}

	return 0;
}
