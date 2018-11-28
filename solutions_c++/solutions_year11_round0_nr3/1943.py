//============================================================================
// Name        : gcj@2011-QR-C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#define N 1005
using namespace std;

int num[N];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int index = 1;
	int t;
	scanf ("%d", &t);
	while (t --) {
		int sum = 0;
		int minNum = 99999999;
		int tmp = 0;
		int n;
		scanf ("%d", &n);
		for (int i = 0; i < n; i ++) {
			int tt;
			scanf ("%d", &tt);
			minNum = min(minNum, tt);
			sum += tt;
			tmp ^= tt;
		}
		printf ("Case #%d: ", index ++);
		if (tmp == 0) {
			printf ("%d\n", sum - minNum);
		} else {
			puts("NO");
		}
	}
	return 0;
}
