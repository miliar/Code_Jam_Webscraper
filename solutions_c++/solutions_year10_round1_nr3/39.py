#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;
LL cache[1000005];

int play(int a, int b) { // a >= b
	if (a==b) return 0;
	if (b == 0) return 0;
	if (a/b > 1) return 1;
	return (play(b, a % b) == 0) ? 1 : 0;
}

LL solve(LL a1, LL a2, LL b1, LL b2) {
	LL ans = 0;
	for (LL i=a1;i<=a2;++i) if (i>1) {
		if (cache[i] == -1) {
			LL lo = 1, hi = i-1, best = 1;
			while (lo <= hi) {
				LL mid = (lo+hi)/2;
				if (play(i,mid)) best = mid, lo = mid+1;
				else hi = mid-1;
			}
			cache[i] = best;
		}
		LL best = cache[i];
		LL upper = min(best,b2);
		LL lower = max(1LL, b1);
		LL add = max(0LL, upper-lower+1);
		ans += add;
	}
	return ans;
}

int main() {
	memset(cache,-1,sizeof cache);
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		LL a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		LL ans = 0;
		ans += solve(a1,a2,b1,b2);
		ans += solve(b1,b2,a1,a2);
		printf("Case #%d: %lld\n", z, ans);
	}
}
