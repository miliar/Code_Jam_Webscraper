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

#define SZ 1024

ll sm[SZ*2];
int sl[SZ*2];
int si[SZ*2];
int g[SZ*2];

int main() {
	int t, tn;
	int i, j, r, k, n;
	ll m, cm, tm;
	int cl;
	
	scanf("%d", &tn);
	for (t = 1; t <= tn; t++)  {
		scanf("%d %d %d", &r, &k, &n);
		for (i = 0; i < n; i++)
			scanf("%d", g + i), g[n + i] = g[i];
		
		for (i = 0; i < SZ; i++)
			sm[i] = 0;
		cm = 0; cl = 0;
		for (i = 0; ; i = j % n) {
			m = 0;
			for (j = i; j < i + n; j++) {
				if (m + g[j] > k) break;
				m += g[j];
			}
			cm += m; cl += 1;
			if (sm[i]) break;
			sm[i] = cm; sl[i] = cl; si[cl] = i;
		}
		cm -= sm[i]; cl -= sl[i];
		if (r <= sl[i]) {
			tm = sm[si[r]];
		}
		else {
			r -= sl[i];
			tm = cm * (r / cl);
			tm += sm[si[sl[i] + r % cl]];
		}
		printf("Case #%d: %lld\n", t, tm);
	}
	
	return (0);
} 
