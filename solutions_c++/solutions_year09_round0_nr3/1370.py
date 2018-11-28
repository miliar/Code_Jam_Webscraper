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

string taskname = "cc";

string p = "welcome to code jam";

#define MAXN 512

vector<int> pos[MAXN];

int a[MAXN];
int ta[MAXN];

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	for (int i = 0; i < p.length(); i++) {
		pos[p[i]].push_back(i);
	}

	int tests;
	scanf("%d\n", &tests);
	for (int test = 1; test <= tests; test++) {
		char buf[1000];
		gets(buf);
		cout << "Case #" << test << ": ";
		istringstream ss(buf);
		string text = string(buf); 
		cerr << text << endl;
		int ans = 0;
		memset(a, 0, sizeof(a));
		a[0] = 1;
		for (int i = 0; i < text.length(); i++) {
			char ch = text[i];
			memset(ta, 0, sizeof(ta));
			for (int j = 0; j < pos[ch].size(); j++) {
				int curpos = pos[ch][j];
				ta[curpos + 1] += a[curpos];
			}
			for (int j = 0; j < MAXN; j++) {
				a[j] += ta[j];
				a[j] %= 10000;
			}
		}
		ans = a[p.length()];
		printf("%04d", ans);
		cout << endl;
	}

	return 0;
}
