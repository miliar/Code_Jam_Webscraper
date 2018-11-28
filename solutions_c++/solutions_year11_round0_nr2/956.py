/*
 * B.cpp
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


int join[300][300];
bool bad[300][300];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
    freopen("B-large.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases) {
		clr(join, -1);
		clr(bad, 0);

		int n;
		cin>>n;
		lp(i, n) {
			string str;
			cin>>str;
			join[str[0]][str[1]] = str[2];
			join[str[1]][str[0]] = str[2];
		}
		cin>>n;
		lp(i, n) {
			string str;
			cin>>str;
			bad[str[0]][str[1]] = 1;
			bad[str[1]][str[0]] = 1;
		}

		cin>>n;
		vector<char> q;
		lp(k, n) {
			char ch;
			cin>>ch;

			q.push_back(ch);
			while(sz(q) >= 2) {
				char a = q.back();		q.pop_back();
				char b = q.back();		q.pop_back();
				if(join[a][b] != -1) {
					q.push_back(join[a][b]);
				} else {
					q.push_back(b);
					q.push_back(a);
					break;
				}
			}

			rep(i, q) lpi(j, i+1, sz(q)) {
				if(bad[q[i]][q[j]]) {
					q.clear();
					break;
				}
			}
		}
		cout<<"Case #"<<cc+1<<": [";
		rep(i, q) {
			if(i) cout<<", ";
			cout<<q[i];
		}
		cout<<"]\n";

	}


	return 0;
}
