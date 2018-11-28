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
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).	end();itr++)
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
	freopen("C:/Users/kenji/Desktop/A-large.in", "r", stdin);
	freopen("C:/Users/kenji/Desktop/A-large.out", "w", stdout);

	int t, n;
	scanf("%d", &t);

	REP(i, t) {
		scanf("%d", &n);

		vector<char> timeline;
		vector<int> blue;
		vector<int> orange;

		REP(j, n) {
			int x;
			char r;

			scanf(" %c %d", &r, &x);
			timeline.push_back(r);
			if (r == 'B')
				blue.push_back(x);
			else
				orange.push_back(x);
		}

		int sz = timeline.size();
		int szBlue = blue.size(), szOrange = orange.size();
		int p = 0, q = 0;
		int bpos = 1, opos = 1;
		int ret = 0;

		REP(j, sz) {
			if (timeline[j] == 'B') {
				int pos = blue[p++];
				ret += ABS(pos - bpos) + 1;
				if (q < szOrange) {
					int move = ABS(pos - bpos) + 1;
					if (opos < orange[q])
						opos = min(opos + move, orange[q]);
					else
						opos = max(opos - move, orange[q]);
				}
				bpos = pos;
			} else {
				int pos = orange[q++];
				ret += ABS(pos - opos) + 1;
				if (p < szBlue) {
					int move = ABS(pos - opos) + 1;
					if (bpos < blue[p])
						bpos = min(bpos + move, blue[p]);
					else
						bpos = max(bpos - move, blue[p]);
				}
				opos = pos;
			}
		}
		printf("Case #%d: %d\n", i+1, ret);
	}
	fflush(stdout);
	cerr << "Done!" << endl;

	return 0;
}
