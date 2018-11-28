#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int h = 1000100;

typedef long long ll;

int T;
ll n;
vector<int> p;
int s[h];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (int i = 2; i < h; i++)
		if (s[i] == 0) {
			p.push_back(i);
			for (int j = i + i; j < h; j+=i)
				s[j] = 1;
		}
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		cin >> n;
		int ans = 1;
		for (int i = 0; i < p.size(); i++) {
			int k = p[i];
			ll e = k * (ll) k;
			while (e <= n) {
				e *= (ll) k;
				ans ++;
			}
		}
		if (n == 1)
			ans = 0;
		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}