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

int M;
int best[20000][2];
int gate[20000];
int change[20000];
int res[2][2][2] = {{{0, 1}, {1, 1}}, {{0, 0}, {0, 1}}};

int main() {
	int casos, val, k;
	cin >> casos;
	REP(caso, casos) {
		cin >> M >> val;
		CLEAR(best, 0x3f);
		for (int i = 1; i <= (M-1)/2; i++) cin >> gate[i] >> change[i];
		for (int i = (M-1)/2 + 1; i <= M; i++) {cin >> k; best[i][k] = 0;}
		for (int i = (M-1)/2; i >= 1; i--) {
			REP(h1, 2) REP(h2, 2) best[i][res[gate[i]][h1][h2]] <?= best[2*i][h1] + best[2*i+1][h2];
			if (change[i]) {
				REP(h1, 2) REP(h2, 2) {
					best[i][res[gate[i]^1][h1][h2]] <?= best[2*i][h1] + best[2*i+1][h2] + 1;
				}
			}
			//cout << best[i][0] << " " << best[i][1] << endl;
		}
		if (best[1][val] < 0x3f3f3f3f) {
			cout << "Case #" << caso+1 << ": " << best[1][val] << endl;
		} else {
			cout << "Case #" << caso+1 << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
