#include <cstdio>
#include <algorithm>
#include <queue>
#include <utility>
using namespace std;
typedef pair<int, int> pii;

int t, it, n, maj[4000], co, i, res;
queue<pair<int, int> > qu;
pii one;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for(it = 1; it <= t; ++it) {
		scanf("%d", &n);
		co = 1 << n;
		for(i = 0; i < co; ++i) {
			scanf("%d", &maj[co + i]);
			maj[co + i] = n - maj[co + i];
		}
		for(i = 0; ++i < co; scanf("%*d"));
		for(i = co; --i >= 0; maj[i] = max(maj[i * 2], maj[i * 2 + 1]));
		qu.push(pii(1, 0));
		res = 0;
		while(!qu.empty()) {
			one = qu.front();
			qu.pop();
			if(one.first > co * 2) { continue; }
			if(one.second < maj[one.first]) {
				++res;
				qu.push(pii(one.first * 2, one.second + 1));
				qu.push(pii(one.first * 2 + 1, one.second + 1));
			}
		}
		printf("Case #%d: %d\n", it, res);
	}
	return 0; }