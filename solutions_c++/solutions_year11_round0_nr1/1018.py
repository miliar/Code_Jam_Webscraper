/*
ID: gupan881
PROG: Bot
LANG: C++
*/
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <vector>
#include <stack>
#include <list>
#include <utility>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define MP(x,y) make_pair(x,y)
int
main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, k;
	cin >> t;
	for(k = 1; k <= t; k++) {
		int pa = 1, pb = 1, ta = 0, tb = 0;
		int n, i, j;
		cin >> n;
		for(i = 0; i < n; i++) {
			char c;
			int d;
			cin >> c >> d;
			switch(c) {
				case 'O':
					ta += abs(pa-d)+1;
					if(ta <= tb)
						ta = tb + 1;
					pa = d;
					break;
				case 'B':
					tb += abs(pb-d)+1;
					if(tb <= ta)
						tb = ta + 1;
					pb = d;
					break;
			}
		}
		printf("Case #%d: %d\n", k, max(ta, tb));
	}
	return 0;
}
