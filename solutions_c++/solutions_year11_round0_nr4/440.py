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

int a[1024];
int as[1024];

//double fact[1024];
//double fix[1024];
//
//map<int, double> mem;

double rec(int n) {
	if (n < 2) return 0;
	return n;
	//if (mem.find(n) == mem.end()) {
	//	double e = 1;
	//	for (int k = 0; k < n; k++)
	//		e += rec(k) * fix[k] / fact[n - k];
	//	mem[n] = e / (1 - fix[n]);
	//}
	//return mem[n];
}

int main() {
	int c, t;
	
	//fact[0] = 1;
	//for (int i = 1; i < 1024; i++)
	//	fact[i] = fact[i - 1] * i;
	//
	//fix[0] = 1;
	//for (int i = 1; i < 1024; i++)
	//	fix[i] = fix[i - 1] + ((i & 1) ? -1 : +1) / fact[i];
	//
	//for (int i = 0; i < 20; i++)
	//	printf("%d %lf\n", i, rec(i));
	
	scanf("%d", &t);
	for (c = 1; c <= t; c++) {
		int i, m, n;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%d", a + i);
			as[i] = a[i];
		}
		sort(as, as + n);
		m = 0;
		for (i = 0; i < n; i++)
			if (a[i] != as[i]) m++;
		printf("Case #%d: %.6lf\n", c, rec(m));
	}
	
	return (0);
}
