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
#define REP(i,n) for(typeof(n) i=0; i<(n); ++i)

const int infty = 999999999;

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

void maximize(int &a,int b) { a = max(a,b); }

int n, d;
VVI vine;

int main()
{
	int run, nruns;

	cin >> nruns;

	for(run=1; run<=nruns; run++) {

		cin >> n;
		vine = VVI(n,VI(2));
		REP(i,n) cin >> vine[i][0] >> vine[i][1];
		cin >> d;

		int res = 0;
		VI reach(n,-1);

		reach[0] = vine[0][0];
		REP(i,n) {
			if ( reach[i]==-1 ) continue;
			if ( vine[i][0]+reach[i]>=d ) { res = 1; break; }
			for(int j=i+1; j<n; j++) {
				if ( vine[i][0]+reach[i]>=vine[j][0] ) {
					maximize(reach[j],min(vine[j][1],vine[j][0]-vine[i][0]));
				}
			}
		}

		cout << "Case #" << run << ": ";
		cout << (res ? "YES" : "NO" ) << endl;
	}

	return 0;
}
