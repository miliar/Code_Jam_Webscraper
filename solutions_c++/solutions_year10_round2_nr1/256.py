#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 100005

char c[N];
map<string, int> mp;
int i, j, k, n, m, x, y, z, t, fr;
int res, it, T;
string s;

int main() {
	freopen("small.in", "r", stdin);	freopen("small.out", "w", stdout);
	scanf("%d", &T);
	for (it = 1; it <= T; it ++) {
		scanf("%d%d", &n, &m);

		mp.clear();
		fr = 1;
		res = 0;
		for (i = 0; i < n; i ++) {
			scanf("%s", &c);
			x = 0;
			s.clear();
			for (j = 0; c[j]; j ++) {
				if (c[j] == '/') {
					
				} else {
					s += c[j];
					if (c[j+1] == '/' || c[j+1] == 0) {
						if (mp.find(s) == mp.end()) {
							mp[s] = fr ++;
						}
					}
				}
			}
		}

		for (i = 0; i < m; i ++) {
			scanf("%s", &c);
			x = 0;
			s.clear();
			for (j = 0; c[j]; j ++) {
				if (c[j] == '/') {
					
				} else {
					s += c[j];
					if (c[j+1] == '/' || c[j+1] == 0) {
						if (mp.find(s) == mp.end()) {
							mp[s] = fr ++;
							res ++;
						}
					}
				}
			}
		}

		printf("Case #%d: %d\n", it, res);
	}
	return 0;
}

		