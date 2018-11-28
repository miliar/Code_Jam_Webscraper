/*
 * A.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: Sep 26, 2009
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
#include<stdio.h>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define repi(i, j, n) 		for(int i=(j);i<(int)(n);++i)
#define repd(i, j, n) 		for(int i=(j);i>=(int)(n);--i)
#define repa(v)				repi(i, 0, sz(v)) repi(j, 0, sz(v[i]))
#define rep(i, v)			repi(i, 0, sz(v))
#define lp(i, cnt)			repi(i, 0, cnt)
#define lpi(i, s, cnt)		repi(i, s, cnt)
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

const int OO = (int)1e8;	//Small -> WRONG, Large -> OVERFLOW

const double PI  = acos(-1.0);
const double EPS = (1e-7);

int dcmp(double x, double y) {	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;	}


set< vector<int> > vis;

int go(vector<int> s) {

	vis.clear();
	queue< vector<int> > q;
	q.push(s);

	int dep = 0, sz = 1;
	vector<int> cur = s;
	for (; !q.empty(); ++dep, sz = q.size()) {
		while (sz--) {
			cur = q.front(), q.pop();

		//	rep(i, cur)	cout<<cur[i]<<" ";	cout<<"\n";

			bool pass = 1;
			rep(t, cur) {
				if(cur[t] > t) {
					pass = 0;
					break;
				}
			}

			if(pass) {
				return dep;
			}
			lp(t, sz(cur)-1) {
				swap(cur[t], cur[t+1]);
				if(vis.insert(cur).second)
					q.push(cur);
				swap(cur[t], cur[t+1]);
			}
		}
	}
	return dep;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("a.in", "rt", stdin);
	freopen("a.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases) {
		int n;
		cin>>n;
		vector<int> s;
		lp(i, n) {
			string str;
			cin>>str;
			int k = str.find_last_of('1');
			s.push_back(k);
		}
		int mn = 0;

		for (int i = 0; i < n; ++i) {
			int j;
			for (j = i; j < n; ++j) {
				if(s[j] <= i)
					break;
			}
			mn+= j-i;
			while(j != i)
				swap(s[j-1], s[j]), j--;
		}

		printf("Case #%d: %d\n", cc+1, mn);
	}


	return 0;
}
