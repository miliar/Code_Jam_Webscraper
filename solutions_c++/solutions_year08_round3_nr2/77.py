#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <deque>
#include <memory>
using namespace std;
typedef vector<int> vi;
typedef long long li;
typedef pair<int,int> pi;
#define all(c) c.begin(), c.end()
#define fr(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define mp make_pair
#define INT 2147483647
#define X first
#define Y second
#define sc(a) scanf("%d", &(a))


char str[1000];
li col;


void rec(string s, li cur, li pre, int raz) {
	if (s.empty()) {
		li C = cur;
		cur = C + pre;
		if (!(cur % 2) || !(cur % 3) || !(cur % 5) || !(cur % 7) || !cur) {++col;}
		if (raz)cur = C - pre;
		if (raz && (!(cur % 2) || !(cur % 3) || !(cur % 5) || !(cur % 7) || !cur)){++col;}
		return;
	}
	if (s.empty()) return;
	rec(s.substr(1), cur, pre * 10 + s[0] - '0', raz);
	rec(s.substr(1), cur + pre, s[0] - '0', 1);
	if (raz) rec(s.substr(1), cur - pre, s[0] - '0', raz);
}

int main() {
	freopen("e:\\code\\b\\b-small.in", "r", stdin);
	freopen("e:\\code\\b\\b-small.out", "w", stdout);
	int p, l, i, j, k, t, T, n;
	sc(T);
	for (t = 1; t <= T; ++t) {
		scanf("%s", str);
		string s = str;
		col = 0;
		rec(s.substr(1), 0, s[0] - '0', 0);
		printf("Case #%d: %lld\n", t, col);
	}
	fclose(stdout);
	return 0;
}
