#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
#define foreach(T, x, it) for (T::iterator it = x.begin(); it != x.end(); ++it)
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

int n;

bool Check(char *s, int p) {
	for (int j = p + 1; j < n; ++j)
		if (s[j] == '1') return false;
	return true;
}

void Swap(char *s1, char *s2) {
	for (int i = 0; i < n; ++i) 
		swap(s1[i], s2[i]);
}

void Solve(int num) {
	
	cin >> n;
	char s[100][100];
	for (int i = 0; i < n; ++i) {
		scanf("%s", s[i]);
	}
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		int ix = -1;
		for (int j = i; j < n; ++j) {
			if (Check(s[j], i)) {
				ix = j;
				break;
			}
		}
		assert(ix != -1);
		if (ix == i) continue;
		ans += ix - i;
		for (int j = ix; j - 1 >= i; --j) {
			Swap(s[j], s[j - 1]);
		}
	}
	printf("Case #%d: %d\n", num, ans);
}

int main() {	
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) Solve(i);
	return 0;
}

