#define _CRT_SECURE_NO_DEPRECATE
//#define _CRT_RAND_S

//#include <windows.h>

#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#include <map>
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned char byte;
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

typedef pair<int, int> pii;

char buff[256];

int x[64];
int v[64];

int main() {
	int t, c;
	int i, n, k, b, T;

	
	scanf("%d", &c);
	for (t = 1; t <= c; t++) {
		int s = 0, r = 0;
		scanf("%d %d %d %d", &n, &k, &b, &T);
		for (i = 0; i < n; i++) scanf("%d", x + i);
		for (i = 0; i < n; i++) scanf("%d", v + i);
		for (i = n-1; i >= 0 && k > 0; i--) {
			if (x[i] + v[i] * T >= b)
				r += s, k--;
			else
				s++;
		}
		if (k == 0)
			printf("Case #%d: %d\n", t, r);
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
	
	return (0);
} 
