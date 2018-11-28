/*
 * B.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: Marwan
 */
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstring>
#include <sstream>
#include <complex>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <climits>
#include <set>
#include <map>

using namespace std;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;
#define MP make_pair
#define SZ(x) (int)x.size()

//#define SMALL
#define LARGE

typedef long long ll;
typedef pair<int, int> pii;

int main() {
#ifdef SMALL
	freopen ("B-small.in" , "rt" , stdin);
	freopen ("B-small.txt" , "wt" , stdout);
#endif
#ifdef LARGE
	freopen ("B-large.in" , "rt" , stdin);
	freopen ("B-large.txt" , "wt" , stdout);
#endif
	int T, N, S, P, t[150], ans;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cin >> N >> S >> P;
		for (int j = 0; j < N; ++j)
			cin >> t[j];
		ans = 0;

		for (int j = 0; j < N; ++j) {
			if ((t[j] / 3) + (t[j] % 3 > 0) >= P)
				ans++;
			else if ( S > 0 and (t[j]/3 + (t[j] % 3) >= P
					or (t[j]%3 == 0 and t[j]/3 + 1 >= P and t[j] > 1)))
				ans++, S--;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}
