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

string taskname = "b";

#define MAXN 3000
#define INF 1000000000 

int v[MAXN];
int a[MAXN];
int m[MAXN];

#define MAXP 12

int64 mem[MAXN][MAXP];
int n, p;


int64 get(int v, int k) {
	int64 & ret = mem[v][k];
	if (ret != -1) {
		return ret;
	}
	if (v >= n - 1) {
		int miss = p - k;
		if (a[v] < miss) { 
			ret = INF;
		} else {
			ret = 0;
		}
		return ret;
	}
	int64 v1 = get(2 * v + 1, k + 1) + get(2 * v + 2, k + 1) + a[v];
	int64 v2 = get(2 * v + 1, k) + get(2 * v + 2, k);
	ret = min(v1, v2);
	return ret;
}

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cout << "Case #" << test + 1 << ": ";
		cin >> p;
		n = (1 << p);
		for (int i = 0; i < n; i++) {
			cin >> v[i];
		}

		vector<int> t;
		for (int i = 0; i < n - 1; i++) {
			int tmp;
			cin >> tmp;
			t.push_back(tmp);
		}
		reverse(t.begin(), t.end());
		for (int i = 0; i < n - 1; i++) {
			a[i] = t[i];
		}
		for (int i = n; i < 2 * n; i++) {
			a[i - 1] = v[2 * n - 1 - i];
		}
		for (int i = n; i < 2 * n; i += 2) {
			a[i - 1] = min(a[i - 1], a[i]);
			a[i] = a[i - 1];
		}
		for (int i = 0; i < 2 * n; i++) {
			cerr << a[i] << " ";
		}
		cerr << endl;
		memset(mem, -1, sizeof(mem));
		cout << get(0, 0);		

		cout << endl;
	}

	return 0;
}
