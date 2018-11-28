#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <numeric>
#include <functional>
#include <bitset>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string>
#include <sstream>
#include <iostream>
#include <limits.h>
#include <valarray>
using namespace std;

struct triplet {
	int x, y, z;
	triplet() : x(0), y(0), z(0) {}
	triplet(int _x, int _y, int _z)
		: x(_x), y(_y), z(_z) {}
	bool operator < (const triplet &t) const {
		if (x != t.x) return x < t.x;
		if (y != t.y) return y < t.y;
		return z < t.z;
	}
};

struct state {
	int best;
	int score;
	bool surprising;
	state() : best(-1), score(-1), surprising(false) {}
	state(int _b, int _s, bool _sur = false)
		: best(_b), score(_s), surprising(_sur) {}
	bool operator < (const state &s) const {
		if (best != s.best) return best < s.best;
		return score < s.score;
	}
};

vector<pair<triplet, state> > triplets;

inline void generate() {
	for (int i = 0; i <= 10; ++i)
		for (int j = 0; j <= 10; ++j)
			for (int k = 0; k <= 10; ++k) {
				if (abs(i - j) <= 2 && abs(i - k) <= 2 && abs(j - k) <= 2) {
					triplet nowT = triplet(i, j, k);
					state nowS = state(max(i, max(j, k)), i + j + k);
					if (abs(i - j) == 2 || abs(i - k) == 2 || abs(j - k) == 2)
						nowS.surprising = true;
					triplets.push_back(make_pair(nowT, nowS));
				}
			}
}

int N, S, p;
vector<int> v;


vector<pair<triplet, state> > res;

void solveSmall(int depth, int &cnt) {
	if (depth == N) {
		int nS = 0;
		int nP = 0;
		for (int i = 0; i < N; ++i) {
			if (res[i].second.surprising) ++nS;
			if (res[i].second.best >= p)
				++nP;
		}
		if (nS == S) cnt = max(cnt, nP);
		return;
	}
	for (int i = 0; i < triplets.size(); ++i) {
		if (triplets[i].second.score != v[depth]) continue;
		res[depth] = triplets[i];
		solveSmall(depth + 1, cnt);
	}
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	generate();
	int T; scanf("%d", &T);
	for (int c = 1; T--; ++c) {
		scanf("%d%d%d", &N, &S, &p);
		v = vector<int>(N);
		res = vector<pair<triplet, state> >(N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &v[i]);
		int cnt = INT_MIN;
		solveSmall(0, cnt);
		printf("Case #%d: %d\n", c, cnt);
	}
	return 0;
}