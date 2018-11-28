#define _CRT_SECURE_NO_DEPRECATE
//#define _CRT_RAND_S

//#include <windows.h>
//#include <tchar.h>
//#include <atlbase.h>
//#include <winerror.h>

#include <climits>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <deque>
#include <string>
#include <bitset>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned char byte;
typedef unsigned short ushort;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define SZ (1024 * 1024)
int p[SZ] = {0};

int main() {
	int i, j, m = 0;
	for (i = 2; i < SZ; i++) {
		if (p[i]) continue;
		p[m++] = i;
		if (i > SZ / i) continue;
		for (j = i * i; j < SZ; j += i)
			p[j] = 1;
	}
	
	int cc, C;
	scanf("%d", &C);
	for (cc = 1; cc <= C; cc++) {
		ll n; scanf("%lld", &n);
		int q = (int) sqrt(double(n));
		int r = (n > 1) ? 1 : 0;
		for (i = 0; p[i] <= q; i++) {
			for (ll t = p[i]; t <= n; t *= p[i]) r++;
			r--;
		}
		printf("Case #%d: %lld\n", cc, r);
	}
	return (0);
}
