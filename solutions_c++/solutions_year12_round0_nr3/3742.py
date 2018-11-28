#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>

using namespace std;

int c, n, res, a, b;

int len (int x) {
	int ret = 0;
	while (x > 0) {
		x /= 10;
		ret++;
	}
	return ret;
}

int recycle (int x) {
	set <int> s;
	int p = 1;
	for (int i = 0; i < n; i++) p *= 10;
	p /= 10;
	int k = x;
	for (int i = 0; i < n; i++) {
		k = (k % 10) * p + (k / 10);
		if (k > x && k >= a && k <= b) s.insert (k);
	}
	return s.size();
}

int main () {
	freopen ("input.in", "r", stdin);
	freopen ("output.out", "w", stdout);
	scanf ("%d", &c);
	for (int p = 0; p < c; p++) {
		scanf ("%d %d", &a, &b);
		n = len (a);
		res = 0;
		for (int i = a; i <= b; i++) res += recycle (i);
		printf ("Case #%d: %d\n", p + 1, res);
	}
	return 0;
}