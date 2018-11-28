using namespace std;
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define PB push_back
#define ALL(x) ((x).begin()),((x).end())
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(int i=0; i<(n); ++i)

const int infty = 999999999;

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

#define minim(x,y,i,j) if ( x>y ) { x = y; }
//debug("cost[%d][%d]: %d -> %d\n",i,j,x,y);

int del, ins, m, n;
VI pixels;

const int maxv = 256;

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		cin >> del >> ins >> m >> n;

		pixels = VI(n);
		REP(i,n) cin >> pixels[i];

		VVI cost(n+2,VI(maxv,infty));

		REP(v,maxv) cost[0][v] = 0;

		REP(i,n) {
			int change = 0;
			REP(v,maxv) {
				// use with (changed) value v1
				REP(v1,maxv)
				    if ( abs(v1-v)<=m ) minim(cost[i+1][v1], cost[i][v] + abs(v1-pixels[i]),i+1,v1);
				// delete
				minim(cost[i+1][v], cost[i][v] + del,i+1,v);
				//insert
				REP(v1,maxv)
				    if ( abs(v1-v)<=m && cost[i][v1] > cost[i][v] + ins ) {
//						debug("cost[%d][%d]: %d -> %d\n",i,v1,cost[i][v1],cost[i][v] + ins);
						cost[i][v1] = cost[i][v] + ins;
						change = 1;
					}
			}

			if ( change ) i--;
		}

		int res = infty;

		REP(v,maxv) minim(res,cost[n][v],-1,-1);

		printf("Case #%d: %d\n",run,res);

//		break;
	}

	return 0;
}
