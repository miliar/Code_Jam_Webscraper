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

#define N 1005

int a[N];
int i, j, k,n ,m, t, T, tt, s, x, y, z, mn;


int main() {
	freopen("c-large.in", "r", stdin);	freopen("c-large.out", "w", stdout);
		
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		scanf("%d", &n);
		x = 0;
		s = 0;
		mn = 1000000000;
		for (i = 0; i < n; i ++) {
			scanf("%d", &a[i]);
			x ^= a[i];
			s += a[i];
			if (a[i] < mn) {
				mn = a[i];
			}
		}
		printf("Case #%d: ", tt);
		if (x != 0) {
			printf("NO\n");
		} else {
			printf("%d\n", s - mn);
		}
	}
	return 0;
}


