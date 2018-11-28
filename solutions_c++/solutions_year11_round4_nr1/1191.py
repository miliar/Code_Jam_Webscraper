#include <string>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define X first
#define SIZE(x) (int)((x).size())

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define SORT(x) sort( (x).begin(), (x).end() ) 


typedef pair<int,int> PII;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

void solve()
{
	int X, S, R, tt, N;

	scanf("%d %d %d %d %d", &X, &S, &R, &tt, &N);
	
	vector<PII> vec;
	REP(i, N) {
		int b, e, w;
		scanf("%d %d %d", &b, &e, &w);

		X -=  (e-b);
		vec.PB( MP(w, (e-b)));
	}
	LD run_tm = 0.0;
	
	vec.PB(MP(0, X));
	
	SORT(vec);
	LD t = (LD)tt;
//	printf("X:%d S: %d \n", X, S);
	REP(i, SIZE(vec)) {
		int speed = vec[i].F;
		LD len = (LD)vec[i].S;

//		printf("len: %.1Lf speed: %d t: %.1Lf run_tm: %.1Lf\n", len, speed, t, run_tm);
		if( (LD)len/(LD)(R+speed) <= t)  {
			t -= (LD)len/(LD)(R+speed);
			run_tm += (LD)len/(LD)(R+speed);
		}
		else {
			LD dist_run = (LD)(R+speed) * t;
			len -= dist_run;

			run_tm += t;
			t = 0.0;
			run_tm += len / (LD)(S+speed);
		}
	}

	printf("%.9Lf\n",run_tm);
}

int main(void)
{
	int T = RI();
	FOR(i,1,T) {
		printf("Case #%d: ", i);
        solve();
	}
	return (0);
}
