//============================================================================
// Name        : goro.cpp
// Author      : TheBigBoss
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
//	freopen("bigA.in", "rt", stdin);
//	freopen("bigA.out", "wt", stdout);
	int n = 0;
	cin >> n;
	for (int N = 1; N <= n; N++) {
		int k = 0, counter = 0, num;
		cin >> k;
		for (int i = 1; i <= k; i++) {
			cin >> num;
			if (num != i)
				counter++;
		}
		printf("Case #%d: %.6lf\n", N, double(counter));
	}
	return 0;
}
