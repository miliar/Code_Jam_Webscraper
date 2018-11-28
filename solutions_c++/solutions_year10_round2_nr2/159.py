#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <sstream>

#define int64 long long

using namespace std;

string taskname = "b";

int n, k, b, t;

#define MAXN 64
#define INF 100000
#define eps 1e-9

pair<int, int> c[MAXN];
int a[MAXN];

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cout << "Case #" << test + 1 << ": ";
		cin >> n >> k >> b >> t;
		for (int i = 0; i < n; i++) {
			cin >> c[i].first;
		}
		for (int i = 0; i < n; i++) {
			cin >> c[i].second;
		}
		sort(c, c + n);
		vector<int> v;
		for (int i = 0; i < n; i++) {
			if (b - c[i].first > c[i].second * t) {
				v.push_back(INF);
			} else {
				int cnt = 0;
				for (int j = i + 1; j < n; j++) {
					int dist = c[j].first - c[i].first;
					int dv = c[i].second - c[j].second;
					if (dist > dv * t) {
						continue;
					}
					double tt = (double)dist / dv;
					if (tt * c[i].second + (t - tt) * c[j].second > b - c[i].first - eps) {
						continue;	
					}
					cnt++;
				}
				v.push_back(cnt);
			}
		}
		sort(v.begin(), v.end());
		int ans = 0;
		for (int i = 0; i < k; i++) {
			ans += v[i];
		}
		if (ans >= INF) {
			cout << "IMPOSSIBLE";
		} else {
			cout << ans;
		}

		cout << endl;
	}

	return 0;
}
