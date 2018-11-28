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

int dx[] = {0, 1, 0, 1};
int dy[] = {0, 0, 1, 1};

VS ret;

bool ck (int x, int y) {
	int r = ret.size();
	int c = ret[0].length();

	REP(i, 4) {
		int xx = x + dx[i];
		int yy = y + dy[i];

		if (xx < 0 || xx >= r || yy < 0 || yy >= c)
			return false;
		if (ret[xx][yy] != '#')
			return false;
	}
	return true;
}

int main() {
	freopen("C:/Users/kenji/Desktop/test.in", "r", stdin);
	freopen("C:/Users/kenji/Desktop/test.out", "w", stdout);

	int t;
	cin >> t;

	REP(ii, t) {
		int r, c;
		cin >> r >> c;
		VS tiles(r);

		REP(i, r)
			cin >> tiles[i];

		ret = tiles;
		bool possible = true;
		REP(i, r) REP(j, c) {
			if (ret[i][j] != '#') continue;
			if (!ck(i, j)) {
				possible = false;
				break;
			}
			ret[i][j] = '/';
			ret[i+1][j+1] = '/';
			ret[i][j+1] = '\\';
			ret[i+1][j] = '\\';

		}
		printf("Case #%d:\n", ii+1);
		if (!possible)
			puts("Impossible");
		else {
			REP(i, r)
				printf("%s\n", ret[i].c_str());
		}
	}

	fflush(stdout);
	cerr << "Done!" << endl;

	return 0;
}
