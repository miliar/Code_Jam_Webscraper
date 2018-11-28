#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <deque>
#include <memory>
using namespace std;
typedef vector<int> vi;
typedef long long li;
typedef pair<int,int> pi;
#define all(c) c.begin(), c.end()
#define fr(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define mp make_pair
#define INT 2147483647
#define X first
#define Y second
#define sc(a) scanf("%d", &(a))


int change[40], and[40];
int em[40], tempand[40], tempmas[40];
int calc(int k, int n, int p) {
	int col = 0, i;
	fr(i, 40) {
		tempand[i] = and[i];
		tempmas[i] = em[i];
	}
	for (i = 0; i < n; ++i) {
		if (1 & (k >> i) && change[i + 1]) {
			++col;
			and[i + 1] = 1 - and[i + 1];
		}
	}
	for (i = n; i >= 1; --i) {
		int sum = em[2 * i + 1] + em[2 * i];
		if ((sum == 2 && and[i]) || (sum > 0 && !and[i])) {
			em[i] = 1;
		}
		else em[i] = 0;
	}
	int f = (em[1] == p);
	fr(i, 40) {
		and[i] = tempand[i];;
		em[i] = tempmas[i];
	}
	if (f) return col;
	return INT;
}

int main() {
	freopen("e:\\code\\a\\a-small.in", "r", stdin);
	freopen("e:\\code\\a\\a-small.out", "w", stdout);
	int i, j, k, n, m, t, T, v, A, x, y, z;
	sc(T);
	fr(t, T) {
		fr(i, 40) change[i] = and[i] = em[i] = 0;
		scanf("%d %d", &n, &v);
		em[1] = v;
		fr(i, (n - 1) / 2) {
			scanf("%d %d", &and[i + 1], &change[i + 1]);
		}
		for (; i < n; ++i) {
			scanf("%d", &em[i + 1]); 
		}
		k = (n - 1) / 2;
		int res = INT;
		for (i = 0; i < (1 << k); ++i) {
			res = min(res, calc(i, k, v));
		}
		if (res == INT) {
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		}
		else printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}
		
