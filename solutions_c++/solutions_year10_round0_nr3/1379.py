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

string taskname = "c";

#define MAXN (1 << 12)

int g[MAXN];
int s[MAXN];
int64 c[MAXN];
int n, r, k;

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cerr << test << endl;
		cout << "Case #" << test + 1 << ": ";
		
		cin >> r >> k >> n;
	
		for (int i = 0; i < n; i++) {
			cin >> g[i];
		}

		for (int i = n; i < 2 * n; i++) {
			g[i] = g[i - n];
		}

		for (int i = 0; i < n; i++) {
			int64 curc = 0;
			for (int j = 0; j <= n; j++) {
				curc += g[(i + j) % n];			
				if (j == n || curc > k) {
					s[i] = (i + j) % n;
					c[i] = curc - g[(i + j) % n];
					break;
				}
			}
		}

/*		for (int i = 0; i < n; i++) {
			cerr << s[i] << " ";
		}
		cerr << endl;

		for (int i = 0; i < n; i++) {
			cerr << c[i] << " ";
		}
		cerr << endl;
*/
		int64 ans = 0;
		int curs = 0;
		for (int i = 0; i < r; i++) {
			ans += c[curs];
			curs = s[curs];
		}
		cout << ans;

		cout << endl;
	}

	return 0;
}
