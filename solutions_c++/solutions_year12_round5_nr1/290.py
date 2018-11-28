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

int l[1000], p[1000], order[1000];

bool cmp(int a, int b) {
	return p[a] < p[b] || p[a] == p[b] && a < b;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test ++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i ++) scanf("%d", &l[i]);
		for (int i = 0; i < n; i ++) {
			scanf("%d", &p[i]);
			p[i] = 100 - p[i];
		}
		for (int i = 0; i < n; i ++) order[i] = i;
		sort(order, order + n, cmp);
		printf("Case #%d:", test + 1);
		for (int i = 0; i < n; i ++) printf(" %d", order[i]);
		printf("\n");
	}
	
	return 0;
}
