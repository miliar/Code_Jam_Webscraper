/*
 * C.cpp
 *
 *  Created on: 2010-6-5
 *      Author: Allie
 */

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <utility>
#include <complex>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>

using namespace std; 

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;

int w;
int h;
bool _b[2][101][101];
bool (*b)[101] = _b[0];
bool (*nb)[101]= _b[1];

int die()
{
	int res = 0;
	bool any;
	do {
		++res;
		any = false;
		for (int y = 1; y <= h; ++y)
			for (int x = 1; x <= w; ++x) {
				nb[y][x] = (!b[y][x] && b[y - 1][x] && b[y][x - 1]) || (b[y][x] && (b[y - 1][x] || b[y][x - 1]));
				if (nb[y][x])
					any = true;
			}
		swap(b, nb);
	} while (any);
	return res;
}

int main() 
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++icase) {
		memset(_b, 0, sizeof(_b));
		w = 0;
		h = 0;
		int R;
		scanf("%d", &R);
		for (int i = 0; i < R; ++i) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			w = max(w, x2);
			h = max(h, y2);
			for (int y = y1; y <= y2; ++y)
				for (int x = x1; x <= x2; ++x)
					b[y][x] = true;
		}
		printf("Case #%d: %d\n", icase, die());
	}
	return 0;
}
