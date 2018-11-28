#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <sstream>

#define int64 long long

using namespace std;

string taskname = "c";

#define MAXN 26

int n;

int rank(int mask, int pos) {
	int ret = 0;
	for (int i = 0; i < pos; i++) {
		if (mask & (1 << i)) {
			ret++;
		}
	}
	return ret;
}

bool check(int mask, int pos) {
	while (1) {
		pos = rank(mask, pos);
		if (pos == 1) {
			return true;
		}
		if (!(mask & (1 << (pos - 1)))) {
			return false;
		}
	}
}

bool good(int mask) {
	return check(mask, n);
}

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cout << "Case #" << test + 1 << ": ";
		cerr << test << endl;	
		cin >> n;
		int cnt = 0;
		for (int i = 0; i < (1 << (n - 1)); i++) {
			if (good(i << 1) && (i & (1 << (n - 2)))) {
				cnt++;
			}
		}
		cout << cnt % 100003;

		cout << endl;
	}

	return 0;
}
