// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <deque>
#include <iomanip>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;

#define rep(i, b, n) for(int i=(b); i<(n); ++i)
#define repd(i, b, n) for(int i=(b); i>(n); --i)
#define trav(it, col) for(typeof((col).begin()) it = (col).begin(); it != (col).end(); ++it)
#define clr(pt) memset((pt), 0, sizeof(pt))
#define EPS 1e-8
#define IFD if(DEBUG)
#define dbg(x) DEBUG && cerr << __LINE__ << ": " << x << endl
#define DL cerr << __LINE__ << endl;
#define mp make_pair

#define DEBUG true

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<double, int> pdi;
typedef pair<double, double> pdd;
typedef stringstream ss;

int INMODE = 0; // 0 specify cases, 1 single run, 2 indefinite runs

bool solve(int cn){
	int n;
	cin >> n;
	cout << "Case #" << cn << ": ";

	vector<pii> v;
	vi best;
	rep(i,0,n)
	{
		int d,l;
		cin >> d >> l;
		v.push_back(pii(d,l));
		best.push_back(0);
	}
	best[0] = v[0].first;
	int D;
	cin >> D;

	bool success = false;
	rep(i,0,n)
	{
		if(v[i].first + best[i] >= D) success = true;
		rep(j,i+1,n)
		{
			if(v[i].first + best[i] >= v[j].first)
			{
				best[j] = max(best[j], min(v[j].second, v[j].first - v[i].first));
			}
			else break;
		}
	}

	if(success) cout << "YES" << endl;
	else cout << "NO" << endl;
	
    return 1;
}

int main(){
    //cout << setiosflags(ios::fixed) << setprecision(10);
    int cases = 1 << 30;
    if(INMODE == 0) cin >> cases;
    if(INMODE == 1) cases = 1;
    for(int cn = 1; cn <= cases; ++cn)
        if(!solve(cn) && INMODE == 2) break;
    return 0;
}


