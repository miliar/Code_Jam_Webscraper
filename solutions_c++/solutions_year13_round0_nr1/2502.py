/*
 * cj2013a.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: ahmedfarag
 */

#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iterator>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>
//#include "vc.h"
//#ifdef _MSC_VER
//	#include <hash_set>
//	#include <hash_map>
//	using namespace stdext;
//#else
//	#if __GNUC__ > 2
//		#include <ext/hash_set>
//		#include <ext/hash_map>
//		using namespace __gnu_cxx;
//	#else
//		#include <hash_set>
//		#include <hash_map>
//	#endif
//#endif

using namespace std;

typedef stringstream ss;
typedef pair<int, int> pii;
typedef long long ll;

#define ALL(x) (x).begin(),(x).end()
#define RALL(x) (x).rbegin(),(x).rend()
#define SZ(x) (int)(x).size()
#define MEMSET(x,val) memset((x),(val),sizeof(x))
#define mp(x,y) make_pair(x,y)

#define OO 1e9
const double PI = acos(-1);
const double EPS = 1e-11;

#define MX 6
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
char b[MX][MX];
int h[MX][MX], v[MX][MX], d1[MX][MX], d2[MX][MX];
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a_small.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);

	for (int tt = 1; tt <= t; ++tt) {
		memset(h, 0, sizeof h);
		memset(v, 0, sizeof v);
		memset(d1, 0, sizeof d1);
		memset(d2, 0, sizeof d2);
		bool incomplete = false;
		for (int i = 0; i < 4; ++i) {
			scanf("%s", b [i]);
			for (int j = 0; j < 4; ++j) {
				if (b[i][j] == '.') {
					incomplete = true;
					continue;
				}
				if (j)
					h[i][j] = h[i][j - 1]
							+ (b[i][j] == b[i][j - 1] || b[i][j] == 'T'
									|| b[i][j - 1] == 'T');
				if (i)
					v[i][j] = v[i - 1][j]
							+ (b[i][j] == b[i - 1][j] || b[i][j] == 'T'
									|| b[i - 1][j] == 'T');
				if (i && j)
					d1[i][j] = d1[i - 1][j - 1]
							+ (b[i][j] == b[i - 1][j - 1] || b[i][j] == 'T'
									|| b[i - 1][j - 1] == 'T');
				if (i && j < 3)
					d2[i][j] = d2[i - 1][j + 1]
							+ (b[i][j] == b[i - 1][j + 1] || b[i][j] == 'T'
									|| b[i - 1][j + 1] == 'T');

			}
		}
 		printf("Case #%d: ", tt);

		int i;
		for (i = 0; i < 4; ++i) {
			if (h[i][3] == 3) {
				printf("%c won\n", b[i][3] == 'T' ? b[i][2] : b[i][3]);
				break;
			}
			if (v[3][i] == 3) {
				printf("%c won\n", b[3][i] == 'T' ? b[2][i] : b[3][i]);
				break;
			}
			if (d1[3][i] == 3) {
				printf("%c won\n", (b[3][i] == 'T' ? b[2][i - 1] : b[3][i]));
				break;
			}
			if (d2[3][i] == 3) {
				printf("%c won\n", b[3][i] == 'T' ? b[2][i + 1] : b[3][i]);
				break;
			}
		}
		if (i == 4) {
			if (incomplete)
				printf("Game has not completed\n");
			else
				printf("Draw\n");
		}
	}

	return 0;
}
