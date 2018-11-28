#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {

	freopen("input.txt.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;

	int s[1111];
	for (int e=1; e<=t; e++) {
		int n; cin >> n;
		for (int u=0; u<n; u++) {
			cin >> s[u];
		}

		int total = 0;
		for (int u=0; u<n; u++)
			total ^= s[u];

		if (total != 0) {
			printf("Case #%d: NO\n", e);
		} else {
			int mn = 0x7f7f7f7f;
			int sum = 0;

			for (int u=0; u<n; u++)
				mn = min(mn, s[u]);

			for (int u=0; u<n; u++)
				sum += s[u];
			sum -= mn;

			printf("Case #%d: %d\n", e, sum);
		}
	}

	return 0;
}