//#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment (linker, "/STACK:100000000")
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>

using namespace std;

//const int INF = 1000000000;
const int INF = 2147483647;
const double eps = 0.000000000001;
const double PI = 3.1415926535897932384626433832795;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) for (int i = 0; i < (int)v.size(); ++i)
#define pb push_back
#define mp make_pair
#define VI vector <int>

int n, a, b, p, N;
int mas[1000];

bool prime(int p) {
	if (p == 1) return false;
	int sq = (int)sqrt((double)p);
	for (int i = 2; i <= sq; ++i)
		if (p % i == 0) return false;
	return true;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	cin >> N;
	forn(test, N) {
		cin >> a >> b >> p;
		memset(mas, 0, sizeof(mas));
		for (int i = 0; i < (b - a + 1); ++i) mas[i] = i;
		while (1) {
			bool fl = false;
			for (int i = a; i <= b; ++i) {
				for (int j = i + 1; j <= b; ++j) {
					if (mas[i - a] == mas[j - a]) continue;
					for (int k = p; k <= i; ++k) {
						if (!prime(k)) continue;
						if (i % k == 0 && j % k == 0) {
							fl = true;
							int tmp = mas[j - a];
							for (int q = 0; q < (b - a + 1); ++q) {
								if (mas[q] == tmp) mas[q] = mas[i - a];
							}
						}
					}
				}
			}
			if (!fl) break;
		}
		int ans = 0;
		bool us[2000];
		memset(us, 0, sizeof(us));
		for (int i = 0; i < (b - a + 1); ++i) 
			if (!us[mas[i]]) {
				++ans;
				us[mas[i]] = true;
			}
		printf("Case #%d: %d\n", test + 1, ans);
	}
	

	return 0;
}

 
