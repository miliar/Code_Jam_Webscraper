#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MOD 10000

string h = "welcome to code jam";
int hn = h.length();
int a[510][20];

int main() {
	#ifndef ONLINE_JUDGE
	freopen("solution.in", "rt", stdin);
	freopen("solution.out", "wt", stdout);
	#endif
	int tests;
	scanf("%d\n", &tests);
	for (int test = 1; test <= tests; test++) {
		string s;
		getline(cin, s);
		int n = s.length();
		for (int i = 1; i <= n; i++) {
			a[i][0] = a[i - 1][0] + (s[i - 1] == h[0]);
			for (int j = 1; j < hn; j++) {
				a[i][j] = a[i - 1][j];
				if (s[i - 1] == h[j]) {
					a[i][j] = (a[i][j] + a[i - 1][j - 1]) % MOD;
				}
			}
		}
		printf("Case #%d: %04d\n", test, a[n][hn - 1]);
	}
	return 0;
}
