/*
 * A.cpp
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

void move(int &i, int &j) {
	if(i < j)
		i++;
	if(i > j)
		i--;
	//or stay
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
    freopen("A-large.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases) {

		int n;
		cin>>n;

		vector< pair<char, int> > v;

		lp(i, n) {
			char a;
			int p;
			cin>>a>>p;
			v.push_back( make_pair(a, p-1));
		}
		int ans = 0;
		int O = 0, B = 0, idx = 0;


		while(idx < n) {
			int anyPush = 0;
			if(v[idx].first == 'O') {
				if(v[idx].second == O)
					anyPush = 1;
				else
					move(O, v[idx].second);
				for (int k = idx+1; k < n; ++k) if(v[k].first == 'B') {
					move(B, v[k].second);
					break;
				}
			} else {
				if(v[idx].second == B)
					anyPush = 1;
				else
					move(B, v[idx].second);
				for (int k = idx+1; k < n; ++k) if(v[k].first == 'O') {
					move(O, v[k].second);
					break;
				}
			}
			idx += anyPush;
			ans++;
		}



		printf("Case #%d: %d\n", cc+1, ans);
	}

	return 0;
}
