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
		int l, h;

		cin >> n >> l >> h;
		vector<int> nums(n);
		REP(i, n)
			cin >> nums[i];

		printf("Case #%d: ", ii+1);
		if (l == 1) {
			puts("1");
			continue;
		}

		bool ck = false;
		int ret;
		for (ret = l; ret <= h; ret++) {
			bool ck2 = true;
			REP(i, n) {
				int mx = max(ret, nums[i]);
				int mn = min(ret, nums[i]);

				if (mx % mn) {
					ck2 = false;
					break;
				}
			}
			if (ck2) {
				ck = true;
				break;
			}
		}
		if (!ck)
			puts("NO");
		else
			printf("%d\n", ret);
	}

	fflush(stdout);
	cerr << "Done!" << endl;

	return 0;
}
