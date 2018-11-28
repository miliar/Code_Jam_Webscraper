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

int main() {
	int c, t;
	
	scanf("%d", &t);
	for (c = 1; c <= t; c++) {
		int i, n;
		int a, as = 0, ax = 0, am = 1000000000;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%d", &a);
			as += a;
			ax ^= a;
			am = min(am, a);
		}
		printf("Case #%d: ", c);
		if (ax == 0)
			printf("%d\n", as - am);
		else
			printf("NO\n");
	}
	
	return (0);
}
