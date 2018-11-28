/*
 * A.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: May 21, 2011
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

int n;
vector<double> calc(vector<string> & v) {
	vector<double> WP(n);
	rep(i, v)
	{
		double a = 0, b = 0;
		rep(j, v[i]) {
			if(v[i][j] != '.') {
				a++;
				if(v[i][j] == '1') {
					b++;
				}
			}
		}
		if(a)
			WP[i] = b / a;
	}
	return WP;
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
		cin>>n;
		vector<string> v(n);
		rep(i, v)
			cin>>v[i];

		vector<double> WP = calc(v);


		cout<<"Case #"<<cc+1<<":\n";
		vector<double> OWP(n);
		double tot = 0;
		rep(i, v) {
			vector<string> cpy = v;
			rep(j, v[i])	cpy[i][j] = '.';
			rep(j, v)		cpy[j][i] = '.';
			vector<double> t = calc(cpy);

			double sum = 0;
			int k = 0;

			rep(j, t)	if(v[i][j] != '.')	{
				sum += t[j];
				k++;
			}
			OWP[i] = sum / k;
			tot += OWP[i];
		}
		vector<double> OOWP(n);
		rep(i, OOWP) {
			int k = 0;
			rep(j, v) if(v[i][j] != '.') {
				OOWP[i] += OWP[j];
				k++;
			}
			OOWP[i] /= k;
		}

		rep(i, v) {
			cout<< 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]<<"\n";
		}

	}

	return 0;
}
