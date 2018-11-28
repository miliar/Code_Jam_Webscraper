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

const double PI = acos(-1.0);

int main() {
	freopen("C:/Users/kenji/Desktop/test.in", "r", stdin);
	freopen("C:/Users/kenji/Desktop/test.out", "w", stdout);

	int cs;
	cin >> cs;

	REP(ii, cs) {
		int n, l, c;
		long long int t;

		cin >> l >> t >> n >> c;
		VI dist(c);

		REP(i, c)
			cin >> dist[i];

		long long int tneed = 0;
		int pos = 0;
		bool ck = false;
		VI boost;
		for (; pos < n; pos++) {
			tneed += 2 * dist[pos % c];
			if (tneed >= t) {
				ck = true;
				if (tneed - t > 0) {
					int rm = (int)(tneed - t);
					boost.push_back(rm);
					if (pos < n)
						++pos;
				}
				break;
			}
		}

		for (; pos < n; pos++)
			boost.push_back(2 * dist[pos % c]);

		sort(ALL(boost), greater<int>());
		long long int tshort = 0;
		REP(i, l)
			tshort += boost[i];
		long long int ret = 0;
		REP(i, n)
			ret += 2 * dist[i%c];
		ret -= tshort/2;

		cout << "Case #" << (ii+1) << ": ";
		cout << ret << endl;
	}

	fflush(stdout);
	cerr << "Done!" << endl;

	return 0;
}
