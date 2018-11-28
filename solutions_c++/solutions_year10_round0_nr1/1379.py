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

string taskname = "ta";

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cout << "Case #" << test + 1 << ": ";
		int n, k;
		cin >> n >> k;
		bool ok = true;
		for (int i = 0; i < n; i++) {
			if (!(k & (1 << i))) {
				ok = false;
				break;
			}
		}
		if (ok) {
			cout << "ON";
		} else {
			cout << "OFF";
		}
		cout << endl;
	}

	return 0;
}
