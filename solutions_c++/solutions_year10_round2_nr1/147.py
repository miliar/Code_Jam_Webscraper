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

string taskname = "aa";

#define MAXN 100000

struct node {
	map<string, int> edges;

	void clear() {
		edges.clear();
	}
};

int pool = 0;
node a[MAXN];
int n, m;


int nodes() {
	return pool;
}

void addnode(string s) {
	s += "/";
	int cur = 0;
	string curs = "";
	for (int i = 1; i < s.length(); i++) {
		if (s[i] == '/') {
			if (a[cur].edges.count(curs)) {
				cur = a[cur].edges[curs];
			} else {
				a[cur].edges[curs] = pool;
				cur = pool;
				pool++;
			}
			curs = "";
		} else {
			curs += s[i];
		}
	}
}

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		for (int i = 0; i < MAXN; i++) {
			a[i].clear();
		}
		pool = 1;
		cout << "Case #" << test + 1 << ": ";
		scanf("%d %d\n", &n, &m);
		for (int i = 0; i < n; i++) {
			char buf[1000];
			gets(buf);
			addnode((string)buf);
		}
		int n1 = nodes();
		for (int i = 0; i < m; i++) {
			char buf[1000];
			gets(buf);
			addnode((string)buf);
		}
		int n2 = nodes();
		cerr << n1 << " " << n2 << endl;
		cout << n2 - n1;
		
		cout << endl;
	}

	return 0;
}
