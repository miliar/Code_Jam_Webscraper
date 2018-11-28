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

	int t;
	cin >> t;

	REP(ii, t) {
		int n;
		cin >> n;

		VS fights(n);
		REP(i, n)
			cin >> fights[i];

		int win[n];
		int cnt[n];
		double OWP[n];
		double OOWP[n];

		REP(i, n) {
			win[i] = cnt[i] = 0;
			REP(j, n) {
				if (j == i) continue;
				if (fights[i][j] == '.')
					continue;
				cnt[i]++;
				if (fights[i][j] == '1')
					++win[i];
			}
		}

		REP(i, n) {
			OWP[i] = 0.0;
			int tmp = 0;
			REP(j, n) {
				if (i == j) continue;
				if (fights[i][j] == '.') continue;
				if (cnt[j]-1 <= 0) continue;
				tmp++;
				if (fights[i][j] == '1') {
					OWP[i] += max(0.0, 1.*(win[j])/(cnt[j]-1));
				}
				else
					OWP[i] += max(0.0, 1.*(win[j]-1)/(cnt[j]-1));
			}
			if (tmp)
				OWP[i] /= tmp;
		}

		REP(i, n) {
			OOWP[i] = 0.0;
			int tmp = 0;
			REP(j, n) {
				if (i == j || fights[i][j] == '.') continue;
				tmp++;
				OOWP[i] += OWP[j];
			}
			if (tmp)
				OOWP[i] /= tmp;
		}

		printf("Case #%d:\n", ii+1);
		REP(i, n) {
			double WP;
			if (cnt[i] == 0)
				WP = 0.0;
			else
				WP = 1.*win[i]/cnt[i];
			printf("%lf\n", 0.25*WP + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}
	}

	fflush(stdout);
	cerr << "Done!" << endl;

	return 0;
}
