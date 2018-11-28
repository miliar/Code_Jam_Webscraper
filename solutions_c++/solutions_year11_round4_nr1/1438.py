#include <algorithm>
#include <cstdio>
#include <iostream>
#include <limits.h>
#include <list>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>

using namespace std;

#define ALL(a)  (a).begin(),(a).end()
#define REP(i, n) for(int i=0; i<(int)(n); i++)
#define FOR(i, s, e) for (int i = (int)(s); i < (int)(e); i++)
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define INF 999999999
#define ABS(x) ((x) < 0 ? - (x) : (x))
#define SIZE(buff) (sizeof(buff)/sizeof(buff[0]))
#define SORT(c) sort((c).begin(),(c).end())
#define PB push_back
#define MP make_pair
#define DISP(x) cout << #x << " : " << x << endl

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long int LL;
typedef pair<double, pair<int, int> >PDI;

const double PI = acos(-1.0);

double v[1100000];

int main() {
	freopen("C:/Users/kenji/Desktop/test.in", "r", stdin);
	freopen("C:/Users/kenji/Desktop/test.out", "w", stdout);
	int t;

	scanf("%d", &t);
	REP(ii, t) {
		int X, S, R, t, N;

		scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
		vector<int> B(N), E(N), w(N);

		REP(i, X) v[i] = S;
		REP(i, N) {
			scanf("%d %d %d", &B[i], &E[i], &w[i]);

			for (int j = B[i]; j < E[i]; j++)
				v[j] = w[i] + S;
		}

		sort(v, v+X);

		double ret = 0.0;
		double tt = 0.0;

		for (int i = 0; i < X; i++) {
			double base = v[i] - S;
			if (tt >= t) {
				ret += 1/v[i];
			}
			else if (tt + 1/(base+R) <= t) {
				tt += 1/(base+R);
				ret += 1/(base+R);
			} else {
				double rm = t - tt;
				tt += rm;
				ret += rm;

				double xt = 1- rm * (base+R);
				ret += xt/v[i];
			}
		}

		printf("Case #%d: %.9lf\n", ii+1, ret);
	}

	fflush(stdout);
	cerr << "Done!" << endl;

	return 0;
}
