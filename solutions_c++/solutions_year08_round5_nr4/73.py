#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

bool rook[200][200];
int ways[200][200];
const int MOD = 10007;
int H, W, R;

int main() {
	int casos, r, c;
	cin >> casos;
	REP(caso, casos) {
		CLEAR(rook, false); CLEAR(ways, 0);
		cin >> H >> W >> R;
		REP(i, R) {
			cin >> r >> c;
			rook[r][c] = true;
		}
		ways[1][1] = 1;
		for (int r = 1; r <= H; r++) {
			for (int c = 1; c <= W; c++) {
				if (!rook[r][c]) {
					if (r > 2 && c > 1) ways[r][c] += ways[r-2][c-1];
					if (r > 1 && c > 2) ways[r][c] += ways[r-1][c-2];
					ways[r][c] %= MOD;
				}
			}
		}
		cout << "Case #" << caso+1 << ": " << ways[H][W] << endl;
	}
	return 0;
}
