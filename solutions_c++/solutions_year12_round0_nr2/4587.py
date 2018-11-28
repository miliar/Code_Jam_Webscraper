// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

#include <algorithm>

using namespace std;

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int t, n, s, p;
	int v[128];

	scanf("%d", &t);

	for (int test = 1; test <= t; ++test) {
		scanf ("%d %d %d", &n, &s, &p);
		for (int i = 0; i < n; ++i) {
			scanf ("%d", &v[i]);
		}
		sort(v, v + n);
		int sol = 0;
		for (int i = n - 1; i >= 0; --i) {
			if (v[i] >= max(3 * p - 2, p)) {
				++sol;
			} else {
				if (s && v[i] >= max(3 * p - 4, p)) {
					--s;
					++sol;
				}
			}
		}
		printf("Case #%d: %d\n", test, sol);
	}

	return 0;
}

