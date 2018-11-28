#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<=(b); i++)
#define FORD(i, b, a) for(int i=(b); i>=(a); i--)
#define FORE(ty, it, data) for(ty::iterator it=data.begin(); it!=data.end(); it++)
#define ALL(x) (x).begin(),(x).end()
#define TWO(X) (1<<(X))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define EPS 1e-10
const double PI = acos(-1.0);

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef map<string, int> MSI;

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }

////////////////////////////////////////////////////////////////////////////////////////////////////////

int x[10], y[10], r[10];

int dd[3][3] = {{0,1,2}, {0,2,1}, {1,2,0}};

double dis(int x0, int y0, int x1, int y1) {
	return sqrt( (double) ((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0)) );
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);

		int n;
		scanf("%d", &n);
		REP(i, n) {
			scanf("%d %d %d", &x[i],&y[i],&r[i]);
		}

		double sol = (double)INT_MAX;

		if(n==1) {
			sol = r[0];
		}
		else if(n==2) {
			sol = max(r[0], r[1]);
		}
		else if(n==3) {
			REP(g, 3) {
				int i = dd[g][0];
				int j = dd[g][1];
				int k = dd[g][2];
				double here1 = r[k];
				double here2 = ( dis(x[i],y[i],x[j],y[j]) + r[i] + r[j] ) / 2.f;
				double here = max(here1, here2);
				sol = min(sol, (double)here);
			}
		}

		printf("%lf\n", sol);
		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}