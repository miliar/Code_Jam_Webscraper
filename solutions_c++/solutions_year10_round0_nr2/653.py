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

string taskname = "tb";

#define MAXN 10

int a[MAXN];
int n;

int gcd(int a, int b) {
	return (b == 0) ? a : gcd(b, a % b);
}

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cout << "Case #" << test + 1 << ": ";
		
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		sort(a, a + n);
		int ret;
		vector<int> v;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < i; j++) {
				v.push_back(a[i] - a[j]);
			}
		}
		ret = v[0];
		for (int i = 1; i < v.size(); i++) {
			ret = gcd(ret, v[i]);
		}
		
		cout << (-(a[n - 1] % ret) + ret) % ret;

		cout << endl;
	}

	return 0;
}
