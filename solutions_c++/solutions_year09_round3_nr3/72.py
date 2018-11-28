#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>

using namespace std;

void submit() {
	freopen("D:\\Codejam\\problem\\problem\\input.in", "r", stdin);
    freopen("D:\\Codejam\\problem\\problem\\output.out", "w", stdout);
}

//code here

char exist[128];
int next[10001];
map<pair<int, int>, int> dp;

int search(int from, int to) {
	if (to <= from) return 0;
	const pair<int,int> key = make_pair(from, to);
	if (dp.count(key) )
		return dp[key];
	int best = 0, luck = from;
	for (luck = next[luck]; luck != -1 && luck <= to; luck = luck < to ? next[luck+1] : -1) {
		int total = to - from;
		total += search(from, luck-1) + search(luck+1, to);
		if (best == 0 || best > total)
			best = total;
	}
	return dp[key] = best;
}

int main() {
	submit();
	int T;
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
		int P, Q;
		scanf("%d %d", &P, &Q);
		memset(next, -1, sizeof next);
		for (int i=0; i<Q; ++i) {
			int t;
			scanf("%d", &t);
			next[t] = t;
		}

		for (int i=P, luck=-1; i>=1; --i) {
			if (next[i] == i)
				luck = i;
			else
				next[i] = luck;
		}

		dp.clear();
		int best = search(1, P);
		printf("Case #%d: %d\n", tid, best);
	}
	return 0;
}