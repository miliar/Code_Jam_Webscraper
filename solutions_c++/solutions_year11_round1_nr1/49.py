#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

int64 n;
int64 pd, pg;

int64 gcd(int64 a, int64 b) {
	return (b ? gcd(b, a%b) : a);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%I64d%I64d%I64d", &n, &pd, &pg);
		
		bool good = false;

		if (pg == 0) {
			if (pd == 0) good = true;
			else good = false;
		}
		else if (pg == 100) {
			if (pd == 100) good = true;
			else good = false;
		}
		else {
			int64 divd = 100 / gcd(100, pd);
			int64 divg = 100 / gcd(100, pg);
			if (divd <= n) good = true;
			else good = false;
		}


		printf("Case #%d: %s\n", tt, (good ? "Possible" : "Broken"));
		fflush(stdout);
	}
	return 0;
}
