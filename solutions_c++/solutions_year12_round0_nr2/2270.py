//============================================================================
// Name        : Qua-A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

bool check(int x, int p) {
	return (x >= 3 * p - 2);
}
bool check2(int x, int p) {
	if (p >= 2)
		return x >= (3 * p - 4);
	else if (p == 1) {
		return x >= 1;
	} else
		return true;
}
int a[110];
int main() {
	freopen("/home/panda/program/input", "r", stdin);
	freopen("/home/panda/program/output", "w", stdout);
	int nc, c;
	int n, s, p, ans;
	scanf("%d", &nc);
	for (c = 1; c <= nc; ++c) {
		scanf("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		ans = 0;
		for (int i = 0; i < n; ++i) {
			if (check(a[i], p)) {
				ans++;
			} else if (s > 0) {
				if (check2(a[i], p)) {
					ans++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}
