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

struct Item {
	int num, count;
	Item(int n = 0, int c = 0): num(n), count(c) {};
};

int n, r, k;
vector<Item> v;
bool us[1005];

void solve(int t) {
	mset(us, 0);
	cin >> r >> k >> n;
	v.clear();
	v.reserve(n);
	int c;
	f(i, 1, n) {
		cin >> c;
		v.pb(Item(i, c));
	}
	lint ans = 0;
	int cur = 1;
	vint moo, cost;
	us[1] = 1;
	moo.pb(1);
	cost.pb(0);
	while (cur <= r) {
		int sum = 0;
		int end = -1;
		while (end + 1 < n && sum + v[end + 1].count <= k) {
			sum += v[end + 1].count;
			++end;
		}
		end = (end + 1) % n;
		rotate(v.begin(), v.begin() + end, v.end());
		ans += sum;
		cost.pb(sum);
		int num = v.front().num;
		moo.pb(num);
		++cur;
		if (us[num]) {
			break;
		}
		us[num] = 1;
	}
	if (cur > r) {
		printf("Case #%d: %lld\n", t, ans);
		return;
	}
	int len = 0;
	lint C = 0;
	int idx = cur - 1;
	while (idx == cur - 1 || moo[idx] != moo[cur - 1]) {
		C += cost[idx];
		--idx;
		++len;
	}
	int ost = r - (cur - 1);
	ans += (lint)(ost / len) * (lint)C;
	ost %= len;
	while (ost) {
		int sum = 0;
		int end = -1;
		while (end + 1 < n && sum + v[end + 1].count <= k) {
			sum += v[end + 1].count;
			++end;
		}
		end = (end + 1) % n;
		rotate(v.begin(), v.begin() + end, v.end());
		ans += sum;
		--ost;
	}
	printf("Case #%d: %lld\n", t, ans);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	f(i, 1, t) solve(i);
	return 0;
}
