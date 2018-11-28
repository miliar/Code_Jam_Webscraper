/*
 * A.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: Sep 3, 2009
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

bool has[30][30];

int main()
{
	freopen("al.in", "rt", stdin);
	freopen("al.out", "wt", stdout);

	int l, d, n;
	cin>>l>>d>>n;
	vector<string> word(d);

	lp(i, d)	cin>>word[i];


	int cc = 1;
	lp(tt, n) {
		int ans = 0;
		string test;
		cin>>test;

		clr(has, 0);

		int k = 0, idx = 0;
		while(k < sz(test)) {
			if(test[k] != '(')
				has[idx][test[k]-'a'] = 1;
			else
				while(test[++k] != ')')
					has[idx][test[k]-'a'] = 1;
			idx++, k++;
		}

		lp(j, d) {
			int valid = 1;
			rep(k, word[j]) {
				if( !has[k][ word[j][k]-'a' ]) {
					valid = 0;
					break;
				}
			}
			ans += valid;
		}

		cout<<"Case #"<<cc++<<": "<<ans<<"\n";

	}



	return 0;
}
