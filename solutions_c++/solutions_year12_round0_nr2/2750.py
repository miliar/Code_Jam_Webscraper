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

int t[30];

bool used[200];

bool surprised(int x) {
	for(int i = 0; i <= 10; i ++) {
		for(int j = 0; j <= 10; j ++) {
			int k = x - i - j;
			if (k < 0 || k > 10)
				continue;
			if (abs(i - j) > 2 || abs(i - k) > 2 || abs(j - k) > 2)
				continue;
			if (abs(i - j) == 2 || abs(i - k) == 2 || abs(j - k) == 2)
				return true;
		}
	}
	return false;
}

bool norm(int x) {
	for(int i = 0; i <= 10; i ++) {
		for(int j = 0; j <= 10; j ++) {
			int k = x - i - j;
			if (k < 0 || k > 10)
				continue;
			if (abs(i - j) > 2 || abs(i - k) > 2 || abs(j - k) > 2)
				continue;
			if (abs(i - j) < 2 && abs(i - k) < 2 && abs(j - k) < 2)
				return true;
		}
	}
	return false;
}

bool surprised(int x, int p) {
	for(int i = 0; i <= 10; i ++) {
		for(int j = 0; j <= 10; j ++) {
			int k = x - i - j;
			if (k < 0 || k > 10)
				continue;
			if (abs(i - j) > 2 || abs(i - k) > 2 || abs(j - k) > 2)
				continue;
			if ((abs(i - j) == 2 || abs(i - k) == 2 || abs(j - k) == 2) && max(max(i, j), k) >= p)
				return true;
		}
	}
	return false;
}

bool norm(int x, int p) {
	for(int i = 0; i <= 10; i ++) {
		for(int j = 0; j <= 10; j ++) {
			int k = x - i - j;
			if (k < 0 || k > 10)
				continue;
			if (abs(i - j) > 2 || abs(i - k) > 2 || abs(j - k) > 2)
				continue;
			if ((abs(i - j) < 2 && abs(i - k) < 2 && abs(j - k) < 2) && max(max(i, j), k) >= p)
				return true;
		}
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i ++) {
		int n, s, p, ans = 0;
		cin >> n >> s >> p;
		for(int j = 0; j < n; j ++)
			cin >> t[j];
		fill(&used[0], &used[0] + 200, false);
		for(int j = 0; j < n; j ++) {
			if (used[j])
				continue;
			if (s && surprised(t[j], p) && !norm(t[j], p)) {
				used[j] = true;
				s --;
				ans ++;
			}
			else if (s && surprised(t[j]) && !norm(t[j]) && !norm(t[j], p)) {
				used[j] = true;
				s --;
				ans ++;
			}
		}
		for(int j = 0; j < n; j ++) {
			if (used[j])
				continue;
			if (s && surprised(t[j], p)) {
				used[j] = true;
				s --;
				ans ++;
			}
		}
		for(int j = 0; j < n; j ++) {
			if (used[j])
				continue;
			if (s && surprised(t[j])) {
				used[j] = true;
				s --;
			}
		}
		for(int j = 0; j < n; j ++) {
			if (used[j])
				continue;
			if (norm(t[j], p))
				ans ++;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}