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

template<class T> void minimize(T &a, T b) { a = min(a,b); }
template<class T> void maximize(T &a, T b) { a = max(a,b); }

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

int n;

struct level {
	int pos;
	int L, P;
	double c;
};

int operator <(level a, level b)
{
	if ( a.L==b.L && a.P==b.P ) return a.pos < b.pos;
	return a.c > b.c;
};

int main()
{
	int run, nruns;

	cin >> nruns;

	for(run=1; run<=nruns; run++) {

		cin >> n;
		vector<level> lev(n);
		REP(i,n) { cin >> lev[i].L; lev[i].pos = i; }
		REP(i,n) {
			cin >> lev[i].P;
			lev[i].c = -log(100-lev[i].P)/lev[i].L;
//			debug("level %d: c = -log(%3d)/%3d = %.4lf\n",i,100-lev[i].P,lev[i].L,lev[i].c);
		}

		sort(ALL(lev));

		cout << "Case #" << run << ":";
		REP(i,n) cout << " " << lev[i].pos;
		cout << endl;
	}

	return 0;
}
