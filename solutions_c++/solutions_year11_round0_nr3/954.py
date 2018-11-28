/*
 * C.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: May 7, 2011
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

typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;
typedef long long         ll;
typedef long double   	  ld;

const ll OO = 1e8;	//Small -> WRONG, Large -> OVERFLOW

const double PI  = acos(-1.0);
const double EPS = (1e-7);

int dcmp(double x, double y) {	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;	}


int main()
{
#ifndef ONLINE_JUDGE
	freopen("C-large.in", "rt", stdin);
    freopen("C-large.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases) {
		int n, Xor = 0, mn = OO, sum = 0;
		cin>>n;
		lp(i, n) {
			int v;
			cin>>v;
			mn = min(mn, v);
			Xor = Xor ^ v;
			sum += v;
		}
		if(Xor != 0)
			printf("Case #%d: NO\n", cc+1);
		else
			printf("Case #%d: %d\n", cc+1, sum-mn);
	}


	return 0;
}
