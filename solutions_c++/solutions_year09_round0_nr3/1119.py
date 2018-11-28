/*
 * c.cpp
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

string wel = "welcome to code jam";

int memo[600][25];
string word;

int cnt(int i, int j)
{
	if(j >= sz(wel))
		return 1;

	if(i >= sz(word))
		return 0;

	int &ret = memo[i][j];
	if(ret != -1)
		return ret;

	ret = 0;

	while(i < sz(word) ) {
		if(word[i] == wel[j]) {
			ret += cnt(i+1, j+1);
			ret %= 10000;
		}
		i++;
	}

	return ret;

}

int main()
{
	freopen("cl.in", "rt", stdin);
	freopen("cl.out", "wt", stdout);

	int cases;
	cin>>cases;
	getline(cin, word);
	lp(cc, cases) {
		getline(cin, word);

		clr(memo, -1);
		int ans = cnt(0, 0);

		ostringstream oss;
		oss<<ans;
		string t = oss.str();
		while(sz(t) < 4)	t = "0" + t;

		cout<<"Case #"<<cc+1<<": "<<t<<"\n";
	}


	return 0;
}
