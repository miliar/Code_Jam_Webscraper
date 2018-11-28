#pragma comment(linker, "/STACK:160777216")
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
#include <ctime>
#include <deque>
#include <climits>
#include <list>
using namespace std;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

long long nextLong() {
	long long x;
	scanf("%lld", &x);
	return x;
}

char buf[1010111];
string nextString() {
	scanf("%s", buf);
	return buf;
}

string nextLine() {
	gets(buf);
	return buf;
}

int main() {
	freopen("C-large.in", "rt", stdin);
	freopen("c_large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		int n = nextInt();
		int s = 0;
		int sum = 0;
		int mn = INT_MAX;
		for (int i = 0; i < n; ++i) {
			int x = nextInt();
			s ^= x;
			sum += x;
			mn = min(mn, x);
		}
		if (s != 0) {
			printf("Case #%d: NO\n", cas);
		} else {
			printf("Case #%d: %d\n", cas, sum - mn);
		}
		cerr << cas << " " << T << endl;
	}
	return 0;
}