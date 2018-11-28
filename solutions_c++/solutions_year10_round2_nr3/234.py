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

#define M 100003
#define SZ 512
int s[SZ] = {0};
int f[SZ][SZ] = {0};

//int a[32];
//int solve_bf(int n) {
//	int i, j, m;
//	int r = 0;
//	for (i = (1 << (n - 2)) - 1; i >= 0; i--) {
//		m = 0;
//		for (j = 0; j < n; j++)
//			if (i & (1 << j)) a[++m] = 2 + j;
//		a[++m] = n;
//		int u = n;
//		for (j = m; j > 0; j--) {
//			if (a[j] < u) break;
//			if (a[j] == u) u = j;
//		}
//		if (u == 1) r++;
//	}
//	return (r);
//}

int main() {
	int t, c;
	
	int m, n;
	f[0][0] = 1;
	for (m = 1; m < SZ; m++) {
		f[0][m] = 1; s[0] = 1;
		for (n = 1; n < SZ; n++) {
			f[n][m] = (s[n - 1] - s[n - min(m, n) - 1] + M) % M;
			s[n] = (s[n - 1] + f[n][m]) % M;
		}
	}
	for (n = 0; n < SZ; n++) {
		s[n] = 0;
		for (m = 0; m <= n; m++)
			s[n] = (s[n] + f[m][n - m]) % M;
	}
	
	scanf("%d", &c);
	for (t = 1; t <= c; t++) {
		scanf("%d", &n);
		printf("Case #%d: %d\n", t, s[n - 1]);
	}
	
	return (0);
} 
