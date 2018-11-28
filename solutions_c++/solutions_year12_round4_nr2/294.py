#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <queue>
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
#include <cstring>
#include <ctime>

using namespace std;

pair<int, int> r[1000], ans[1000];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test ++) {
		int n, w, l;
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 0; i < n; i ++) {
			scanf("%d", &r[i].first);
			r[i].second = i;
		}
		sort(r, r + n);
		int y = 0;
		for (int i = 0, j = 0; i < n; i = j) {
			int sum = 0;
			for (j = i; j < n; j ++) {
				if (j > i) sum += r[j].first;
				if (sum > w) break;
				sum += r[j].first;
			}
			if (i > 0) y += r[j-1].first;
			int x = 0;
			for (int k = i; k < j; k ++) {
				if (k > i) x += r[k].first;
				ans[r[k].second] = make_pair(x, y);
				x += r[k].first;
			}
			y += r[j-1].first;
		}
		printf("Case #%d:", test + 1);
		for (int i = 0; i < n; i ++) {
			printf(" %d %d", ans[i].first, ans[i].second);
			if (ans[i].first > w || ans[i].second > l)
				fprintf(stderr, "jiong\n");
		}
		printf("\n");
	}
	
	return 0;
}
