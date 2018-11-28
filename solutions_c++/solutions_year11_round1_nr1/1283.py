//============================================================================
// Name        : gcj@2011-1A-A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
using namespace std;
typedef long long LL;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T;
	int index = 1;
	scanf ("%d", &T);
	while (T --) {
		int n, pd, pg;
		scanf ("%d%d%d", &n, &pd, &pg);
		printf ("Case #%d: ", index ++);
		if (pd != 100 && pg == 100) {
			puts("Broken");
			continue;
		}
		if (pd != 0 && pg == 0) {
			puts("Broken");
			continue;
		}
		bool flag = false;
		for (int i = 1; i <= n; i ++) {
			if (i * pd % 100 == 0) {
				flag = true;
			}
		}
		if (flag) {
			puts("Possible");
		} else {
			puts("Broken");
		}
	}
	return 0;
}
