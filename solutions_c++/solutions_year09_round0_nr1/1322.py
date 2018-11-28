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

#define MAXL 20
#define MAXN 5010

set<char> a[MAXN][MAXL];
vector<string> v;


int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int l, d, n;

	scanf("%d %d %d\n", &l, &d, &n);
	for (int i = 0; i < d ; i++) {
		char buf[MAXL];
		gets(buf);
		v.push_back(string(buf));
	}

	for (int i = 0; i < n; i++) {
		char buf[1000000];
		gets(buf);
		char cur;
		int pos = 1;
		bool brac = false;
		cur = buf[0];
		for (int j = 0; j < l; j++) {
			while (cur == '(' || cur == ')') {
				if (cur == '(') {
					brac = true;
				}
				cur = buf[pos++];
			}
			while (cur != 0 && cur != ')' && cur != '(') {
				a[i][j].insert(cur);
				cur = buf[pos++];
				if (!brac) {
					break;
				}
			}
			brac = false;
		}
	}

	for (int j = 0; j < n; j++) {
		int ans = 0;
		for (int i = 0;i < d; i++) {
			bool ok = true;
			for (int k = 0; k < l; k++) {
				if (!a[j][k].count(v[i][k])) {
					ok = false;
					break;
				}
			}
			if (ok) {
				ans++;
			}
		}
		cout << "Case #" << (j + 1) << ": " << ans << endl;
	}

	return 0;
}
