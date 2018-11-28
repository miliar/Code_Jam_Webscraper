#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <bitset>
#include <string>
#include <memory>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <cassert>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define s(c) ((int)((c).size()))
#define all(c) (c).begin(),(c).end()
#define mset(a, v) memset(a, v, sizeof(a))
#define f(i, lo, hi) for (int i = (lo), Max = (hi); i <= Max; ++i)
#define rf(i, hi, lo) for (int i = (hi), Min = (lo); i >= Min; --i)
#define c(i, c) f(i, 0, s(c) - 1)
#define rc(i, c) rf(i, s(c) - 1, 0)
#define it(type, it, c) for (type::iterator it = (c).begin(); it != (c).end(); ++it)
#define rit(type, it, c) for (type::reverse_iterator it = (c).rbegin(); it != (c).rend(); ++it)
typedef vector<int> vint;
typedef long long lint;

int n;
char m[42][45];

void solve(int t) {
	printf("Case #%d: ", t);
	scanf("%d", &n);
	f(i, 1, n) {
		scanf("%s", &m[i][1]);
	}
	vint v(n + 1);
	f(i, 1, n) {
		int en = n;
		while (en >= 1 && m[i][en] == '0') --en;
		v[i] = en;
	}
	int ans = 0;
	f(i, 1, n) {
		if (v[i] > i) {
			int f = -1;
			f(j, i + 1, n) {
				if (v[j] <= i) {
					f = j;
					break;
				}
			}
			ans += f - i;
			rf(j, f, i + 1)
				swap(v[j], v[j - 1]);
		}
	}
	printf("%d\n", ans);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	f(i, 1, t)
	solve(i);
	return 0;
}
