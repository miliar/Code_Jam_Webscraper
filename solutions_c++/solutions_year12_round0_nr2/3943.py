#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
int inline ABS(int a){ return a>0?a:-a; }
typedef pair<int,int> pi;
typedef unsigned long long ULL;
typedef long long LL;

/* Main code starts from here */

bool C(int a, int b) {
	if (a >= 0 && a <= 10 && b >= 0 && b <= 10 && abs(a - b) < 2) return true;
	return false;
}

bool CS(int a, int b) {
	if (a >= 0 && a <= 10 && b >= 0 && b <= 10 && abs(a - b) <= 2) return true;
	return false;
}

int gg[128];
int main() {
	int t, T;
	for (scanf("%d", &T), t = 1; t <= T; t++) {
		int n, s, p;
		scanf("%d %d %d", &n, &s, &p);
		for (int i = 0; i < n; i++)
			scanf("%d", &gg[i]);
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			// Try to make best possible p without surprise
			int a,b,c;
			bool pos = false;
			for (a = p; a <= 10; a++) {
				for (b = 0; b <= 10; b++) {
					c = gg[i] - a - b;
					if (C(a, b) && C(a, c) && C(b, c)) {
						pos = true;
					}
				}
			}
			if (pos) {
				cnt ++;
				continue;
			}
			// Use surprise
			if (s > 0) {
				for (a = p; a <= 10; a++) {
					for (b = 0; b <= 10; b++) {
						c = gg[i] - a - b;
						if (CS(a, b) && CS(a, c) && CS(b, c)) {
							pos = true;
						}
					}
				}
			}
			if (pos) {
				--s;
				cnt++;		
			}
		}
		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}
