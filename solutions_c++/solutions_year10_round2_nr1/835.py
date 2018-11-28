/*
 * A.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: May 22, 2010
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

const int OO = (int)1e8;	//Small -> WRONG, Large -> OVERFLOW

const double PI  = acos(-1.0);
const double EPS = (1e-7);

int dcmp(double x, double y) {	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;	}

vector<string> split(string orig, string pat)
{	//split("affbffFFwow", "ff") ->{a, b, FFwow}
	vector<string> v;
	int pos = orig.find(pat);
	while(pos != -1)
	{
		string left = orig.substr(0, pos);
		if(left != "")		// Modify this if needed
			v.push_back(left);
		orig.replace(0, pos+pat.size(), "");
		pos = orig.find(pat);
	}
	if(orig != "")	v.push_back(orig);
	return v;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
    freopen("alarge.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases) {
		int n, m;
		cin>>n>>m;
		set<string> cur;
		lp(i, n) {
			string s;
			cin>>s;
			cur.insert(s);
		}

		int ans = 0;
		lp(i, m) {
			string s;
			cin>>s;
			vector<string> v = split(s, "/");
			string f = "";
			rep(j, v) {
				f += "/"+v[j];
				if(cur.count(f) == 0) {
					ans++;
					cur.insert(f);
				}
			}
		}
		printf("Case #%d: %d\n", cc+1, ans);
	}



	return 0;
}
