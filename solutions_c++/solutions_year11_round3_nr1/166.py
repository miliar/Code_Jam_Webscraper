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

	freopen("inputl.txt.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; cin >> t;
	for (int e=1; e<=t; e++) {
		int n,m; cin >> n >> m;


		char s[55][55];
		for (int i=0; i<n; i++)
			cin >> s[i];

		char d[55][55];
		memcpy(d, s, sizeof s);

		bool can = true;
		for (int i=0; i<n; i++) {
			for (int u=0; u<m; u++) {
				if (s[i][u] == '#') {
					if (s[i+1][u] == '#' && s[i][u+1] == '#' && s[i+1][u+1] == '#') {
						s[i][u] =  '/';
						s[i+1][u] = '\\';
						s[i+1][u+1] = '/';
						s[i][u+1] = '\\';
					} else {
						can = false;
						goto nxt;
					}
				}
			}
		}

nxt:;
		printf("Case #%d:\n", e);
		
		if (can) {
			for (int i=0; i<n; i++)
				printf("%s\n", s[i]);
		} else {
			printf("Impossible\n");
		}
	}	

	return 0;
}
