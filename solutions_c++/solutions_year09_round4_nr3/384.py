#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool compatible(const vector<int> &s1, const vector<int> &s2) {
	int sgn = (s1[0] > s2[0]) ? -1 : 1;
	for(size_t i = 0; i < s1.size(); ++i) {
		if(sgn * (s1[i] - s2[i]) >= 0)
			return false;
	}
	return true;
}

const int inf = (1<<28) + 43;

int best[1<<17];
int Best(int cur, const vector<int> &poss) {
	int &ret = best[cur];
	if(ret != -1)
		return ret;

	//fprintf(stderr, "Best(%d)\n", cur);
	ret = inf;
	for(vector<int>::const_iterator it = poss.begin(); it != poss.end(); ++it) {
		ret = min(ret, 1 + Best(cur & ~(*it), poss));
	}
	return ret;
}

bool solve(int P) {
	int N, K;
	scanf("%d%d", &N, &K);
	vector<vector<int> > stocks;
	for(int i = 0; i < N; ++i) {
		vector<int> s(K);
		for(int k = 0; k < K; ++k) {
			scanf("%d", &s[k]);
		}
		stocks.push_back(s);
	}
	vector<int> poss;
	sort(stocks.begin(), stocks.end());
	memset(best, -1, sizeof(best));
	best[0] = 0;
	for(int i = 0; i < (1 << N); ++i) {
		bool bad = false;
		for(int k = 0; k < N && !bad; ++k) {
			if(!(i & (1 << k)))
				continue;
			for(int j = k + 1; j < N && !bad; ++j) {
				if(!(i & (1 << j)))
					continue;
				if(!compatible(stocks[k], stocks[j]))
					bad = true;
			}
		}
		if(!bad)
			poss.push_back(i);
	}

	queue<int> q;
	q.push(0);
	vector<int> dist(1<<N);
	while(!q.empty()) {
		int cur = q.front();
		q.pop();
	}
	
	fprintf(stderr, "%d\n", P+1);
	printf("Case #%d: %d\n", P + 1, dist[(1<<N) -1]);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
