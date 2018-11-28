#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
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
#include <cstring>
 
using namespace std;

const int MAXN = 2048;

int _t, res, p, two = 2;
int in[MAXN], price[MAXN][MAXN];

bool check(int start, int end) {
	for (int i = start; i < end; i++)
		if (in[i] < p) return false;
	return true;
}

int go(int start, int end, int adj, int level, int pos) {
	int ret = 0;
	if (level == -1 || check(start, end) == true) return ret;
	int mx = 0, a = 1 << 30, b = 1 << 30;
	for (int i = start; i < end; i++) mx = max(mx, p - in[i]);
	if (mx <= level) a = go(start, end - adj, adj / 2, level - 1, pos * 2) + go(start + adj, end, adj / 2, level - 1, pos * 2 + 1);
	b = price[level][pos];
	for (int i = start; i < end; i++) in[i]++;
	b += go(start, end - adj, adj / 2, level - 1, pos * 2) + go(start + adj, end, adj / 2, level - 1, pos * 2 + 1);
	for (int i = start; i < end; i++) in[i]--;
	return min(a, b);
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &_t);
	for (int cas = 1; cas <= _t; cas++) {
		scanf("%d", &p);
		res = 0;
		two = 1;
		for (int i = 1; i <= p; i++) two *= 2;
		for (int i = 0; i < two; i++) scanf("%d", &in[i]);
		for (int i = 0, k = two / 2; i < p; i++) {
			for (int j = 0; j < k; j++) scanf("%d", &price[i][j]);
			k /= 2;
		}
		printf("Case #%d: %d\n", cas, go(0, two, two / 2, p - 1, 0));
	}
	return 0;
}