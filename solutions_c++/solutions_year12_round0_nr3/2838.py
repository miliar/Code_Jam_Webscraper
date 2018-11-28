#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <numeric>
#include <functional>
#include <bitset>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string>
#include <sstream>
#include <iostream>
#include <limits.h>
#include <valarray>
using namespace std;

int A, B;

int numberLen(int n) {
	int cnt = 0;
	while (n) {
		n /= 10;
		++cnt;
	}
	return cnt;
}

int power(int b, int p) {
	int x(1), y(b);
	for (; p > 0; p >>= 1) {
		if (p % 2)
			x *= y;
		y *= y;
	}
	return x;
}

void recycle(int n, int &res) {
	if (n < 10) return;
	int a = n;
	int zero = 0;
	do {
		int back = a % 10;
		a /= 10;
		if (back == 0) {
			++zero;
			continue;
		}
		int front = power(10, numberLen(a) + zero) * back;
		zero = 0;
		a += front;
		if (a != n && a >= A && a <= B) ++res;
	} while (a != n);
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T; cin >> T;
	for (int c = 1; T--; ++c) {
		cin >> A >> B;
		int res = 0;
		for (int n = A; n <= B; ++n)
			recycle(n, res);
		printf("Case #%d: %d\n", c, res >> 1);
	}
	return 0;
}