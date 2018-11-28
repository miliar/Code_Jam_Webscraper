#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <ctime>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <cstring>
#include <set>
#include <deque>
#include <cmath>
#include <stack>

using namespace std;

pair<int, int> s[10010];
long long dp[10010];

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; cin >> t;
	
	for (int e=1; e<=t; e++) {
		int n; cin >> n;
		for (int i=0; i<n; i++)
			cin >> s[i].first >> s[i].second;
		int d; cin >> d;

		memset(dp, -1, sizeof dp);
		
		dp[0] = s[0].first;

		bool can = false;
		for (int i=0; i<n; i++) {
			int cur = dp[i];
			if (s[i].first + cur >= d) {
				can = true;
				break;
			}
			for (int canReach = i+1; canReach < n; canReach++) {
				if (s[canReach].first - s[i].first <= cur) {
					long long other = min(s[canReach].second, s[canReach].first - s[i].first);
					dp[canReach] = max(dp[canReach], other);
				} else break;
			}
		}

		cout << "Case #" << e << ": ";

		cout << (can ? "YES" : "NO");
		cout << endl;
	}

    return 0;
}