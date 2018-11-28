#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

const int dd[4][2] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
const int dd2[4][2] = {{0, 1}, {1, 0}, {1, 1}, {0, 0}};

int h1[10000], h2[10000];
int v1[10000], v2[10000];
bool h[10000], v[10000];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		memset(h, 0, sizeof(h));
		memset(v, 0, sizeof(v));
		int l; scanf("%d", &l);
		int a = 0, b = 0;
		int d = 0, x = 3010, y = 3010;
		h[x] = v[y] = true;
		h1[x] = h2[x] = x;
		v1[y] = v2[y] = y;
		while (l--) {
			int t;
			char s[100];
			scanf("%s %d", s, &t);
			for (int i = 0; i < t; ++i) {
				for (int j = 0; s[j] != 0; ++j) {
					if (s[j] == 'L') d = (d + 1) & 3;
					else if (s[j] == 'R') d = (d + 3) & 3;
					else {
						x += dd[d][0], y += dd[d][1];
						if (!h[y]) h1[y] = h2[y] = x, h[y] = true;
						else {
							if (h1[y] > x) h1[y] = x;
							if (h2[y] < x) h2[y] = x;
						}
						if (!v[x]) v1[x] = v2[x] = y, v[x] = true;
						else {
							if (v1[x] > y) v1[x] = y;
							if (v2[x] < y) v2[x] = y;
						}
						if (d == 1) {
							a += y;
						} else if (d == 3) {
							a -= y;
						}
					}
				}
			}
		}
		a = abs(a);
		for (int i = 0; i < 6020; ++i) {
			for (int j = 0; j < 6020; ++j) {
				bool f = true;
				for (int k = 0; k < 4; ++k) {
					int x = i + dd2[k][0], y = j + dd2[k][1];
					if (h[y] && v[x]) {
						if (((h1[y] <= x) && (h2[y] >= x)) || ((v1[x] <= y) && (v2[x] >= y))) {
						} else {
							f = false;
							break;
						}
					} else {
						f = false;
						break;
					}
				}
				if (f) {
					++b;
				}
			}
		}
		b -= a;
		printf("Case #%d: %d\n", tt + 1, b);
	}
	return 0;
}
