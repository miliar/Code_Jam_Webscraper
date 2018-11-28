#include <cstdio>
#include <set>
#include <algorithm>

using namespace std;

typedef long long lld;

lld digs(lld val) {
	int ct=0;
	do {
		ct++;
	} while (val=val/10);
	return ct;
}

lld powah(lld idx) {
	lld ret = 1;
	for (int i=0; i<idx; i++) {
		ret *= 10;
	}
	return ret;
}

bool mid (lld a, lld b, lld c) {
	return a<=b && b<=c;
}

#define mp make_pair
bool done[3000][3000];

lld explore(lld val, lld a, lld b) {
	lld dig = digs(val), add=0ll;
	lld ptr = val;
	do {
		if (digs(ptr) == dig) {
			if (mid(a, ptr, b) && ptr > val) {
				add++;
			}
		}
		int last = ptr%10;
		ptr /= 10;
		ptr += last*powah(dig-1);
	} while(ptr != val);
	return add;
}
		

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=1; ti<=t; ti++) {
		int a, b;
		scanf("%d%d", &a, &b);
		lld sum = 0;
		for (int i=a; i<=b; i++) {
			sum += explore(i, a, b);
		}
		printf("Case #%d: %lld\n", ti, sum);
	}
	return 0;
}