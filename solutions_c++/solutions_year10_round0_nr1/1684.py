/*
 * A.cpp
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

int solve2(ll n, ll k) {
	ll t = (1LL <<n);
	return k != 0 && (k+1) % t == 0;
}

int solve1(ll n, ll k) {
	vector<int> power(n, 0);
	vector<int> state(n, 0);
	power[0] = 1;

	lp(t, k) {
		rep(i, power)
			if (power[i])
				state[i] = !state[i];
		int j = 0;
		while (j < n && power[j] && state[j])
			j++;
		while (j != 0 && j < n && power[j - 1] && state[j - 1])
			power[j++] = true;
		lpi(i, j+1, n)
			power[i] = false;

	}
	return power[n - 1] && state[n - 1];
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("clarge.txt", "wt", stdout);
#endif

	int cases;
	cin >> cases;

	lp(cc, cases) {
		ll n, k;
		cin >> n >> k;
		bool ans = solve2(n, k);
		if (ans)
			printf("Case #%d: ON\n", cc + 1);
		else
			printf("Case #%d: OFF\n", cc + 1);
	}

	return 0;
}
