#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>
#include <map>

using namespace std;

#define pii pair <int, int>
#define mp make_pair
#define ll long long

int p_pow[20];

inline int calc(int x) {
	int s = 0;
	do {
		s ++;
	} while (x /= 10);
	return s;
}

inline int next(int x, int len) {
	int d = p_pow[len - 1];
	return (x % d) * 10 + x / d;
}

void init() {
	p_pow[0] = 1;
	for(int i = 1; i <= 9; i ++)
		p_pow[i] = p_pow[i - 1] * 10;
}

ll stupid(int a, int b) {
	ll ans = 0;
	for(int i = a; i < b; i ++) {
		for(int j = i + 1; j <= b; j ++) {
			int x = i;
			int len = calc(x);
			do {
				x = next(x, len);
				if (x == j) {
					ans ++;
					x = i;
				}
			} while (x != i);
		}
	}
	return ans;
}

ll solve(int a, int b) {
	ll ans = 0;
	for(int i = a; i < b; i ++) {
		set <int> st;
		int x = i;
		int len = calc(x);
		do {
			x = next(x, len);
			if (x > i && x <= b)
				st.insert(x);
		} while (x != i);
		ans += st.size();
	}
	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	init();
	int n;
	cin >> n;
	for(int i = 0; i < n; i ++) {
		int a, b;
		cin >> a >> b;
		printf("Case #%d: ", i + 1);
		cout << solve(a, b) << endl;
	}
	return 0;
}