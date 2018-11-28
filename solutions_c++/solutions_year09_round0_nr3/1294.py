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
#include <iomanip>
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

char s[512];
int dp[502][20];
char *moo = "welcome to code jam";

int go(int L, int m) {
	if (dp[L][m] != -1)
		return dp[L][m];
	if (m == 0)
		return dp[L][m] = 1;
	int r = 0;
	rf(i, L - 1, 0) if (s[i] == moo[m - 1]) {
		r = (r + go(i, m - 1)) % 10000;
	}
	return dp[L][m] = r;
}

void solve(int t) {
	gets(s);
	mset(dp, -1);
	char b[8];
	ostringstream out(b);
	out << setw(4) << setfill('0') << go(strlen(s), 19);
	printf("Case #%d: %s\n", t, out.str().substr(0, 4).c_str());
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n;
	scanf("%d\n", &n);
	f(i, 1, n)
	solve(i);
	return 0;
}
