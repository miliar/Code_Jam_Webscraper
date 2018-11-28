#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
static const double PI2 = 8.0 * atan(1.0);
typedef long long ll;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define ALL(c) (c).begin(), (c).end()

map<ll, int> cache;
int cost[16][16];

ll makeKey(int pos, int depth, int state[]) {
	ll key = 0;
	for (int i = pos; i < pos + (1 << depth); ++i) {
		key <<= 4;
		key += state[i];
	}
	key <<= 4;
	key += pos;
	key <<= 4;
	key += depth;
	return key;
}

int dfs(int pos, int depth, int state[]) {
	const ll key = makeKey(pos, depth, state);
	if (cache.count(key)) {
		return cache[key];
	}

	ll result = 0;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int P;
		cin >> P;
		vector<int> miss;
		for (int i = 0; i < (1 << P); ++i) {
			int value;
			cin >> value;
			miss.push_back(value);
		}

		for (int i = 0; i < (1 << P) - 1; ++i) {
			int value;
			cin >> value;
		}

		static bool use[16][2 * 2048];
		memset(use, 0, sizeof(use));
		for (int i = 0; i < miss.size(); ++i) {
			int p = i;
			vector<int> pos;
			for (int j = 0; j < P; ++j) {
				p /= 2;
				pos.push_back(p);
			}
			reverse(pos.begin(), pos.end());

			int pp = P;
			for (int j = 0; j < pos.size() && j < P - miss[i] && pp >= 0; ++j) {
				use[pp][pos[j]] = true;
				--pp;
			}
		}

		int answer = 0;
		for (int i = 0; i < 16; ++i) {
			for (int j = 0; j < 2 * 2048; ++j) {
				answer += use[i][j];
			}
		}

		printf("Case #%d: %d\n", t, answer);
	}
}
