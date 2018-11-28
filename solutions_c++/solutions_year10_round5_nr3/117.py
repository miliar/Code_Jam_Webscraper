#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define NEED_BIG_INT 0
#define DEBUG_FLAG 1

#if NEED_BIG_INT
#include <gmpxx.h>
typedef mpz_class bint;
typedef mpq_class brational;
typedef mpf_class bdecimal;
// compile with -lgmpxx -lgmp (may need -lm too)
#endif

#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define cdbg(...)
#define dbg(...)
#endif

int N;
map<int, int> c;

int f() {
	int ans = 0;
	while (true) {
		for (map<int, int>::iterator it = c.begin(); it != c.end(); ++it)
			if (it->second > 1) {
				int p = it->first;
				c[p] -= 2;
				++c[p+1];
				++c[p-1];
				ans++;
				goto hell;
			}
		break;
		hell:;
	}
	return ans;
}

int main() {
	string fname = "C-small-attempt0";
	//string fname = "C-large";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int CASES;
	scanf("%d", &CASES);
	for (int CASE = 1; CASE <= CASES; ++CASE) {
		scanf("%d", &N);
		c.clear();
		for (int i = 0; i < N; ++i) {
			int p, v;
			scanf("%d%d", &p, &v);
			c[p] += v;
		}
		int ans = f();
		printf("Case #%d: %d\n", CASE, ans);
	}

	return 0;
}
