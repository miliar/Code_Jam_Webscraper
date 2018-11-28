#define _CRT_SECURE_NO_DEPRECATE

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

#define SZ 64
char a[SZ][SZ];

int offi[SZ*SZ];
int offj[SZ*SZ];

int chk1(int i1, int j1, int i2, int j2, int n, int i0, int j0) {
	i1 -= i0; if (i1 < 0 || i1 >= n) return (1);
	j1 -= j0; if (j1 < 0 || j1 >= n) return (1);
	i2 -= i0; if (i2 < 0 || i2 >= n) return (1);
	j2 -= j0; if (j2 < 0 || j2 >= n) return (1);
	return (a[i1][j1] == a[i2][j2]);
}

int chk(int n, int n0, int i0, int j0) {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < i; j++) {
			if (!chk1(i, j, j, i, n0, i0, j0)) return (0);
			if (!chk1(n - 1 - i, j, n - 1 - j, i, n0, i0, j0)) return (0);
		}
	}
	return (1);
}

int chk_all(int n, int n0) {
	int i, j;
	for (i = 0; i <= n - n0; i++)
		for (j = 0; j <= n - n0; j++)
			if (chk(n, n0, i, j)) return (1);
	return (0);
}

int main() {
	int t, c;
	int i, j, k, l, n, n2;
	
	scanf("%d", &c);
	for (t = 1; t <= c; t++) {
		scanf("%d", &n);
		
		k = 0;
		for (l = 0; l < n; l++)
			for (j = 0; j <= l; j++)
				offj[k] = j, offi[k] = l - j, k++;
		for (l = n - 2; l >= 0; l--)
			for (j = 0; j <= l; j++)
				offj[k] = n - 1 - l + j, offi[k] = n - 1 - j, k++;

		//for (k = 0; k < n * n; k++)
		//	a[offi[k]][offj[k]] = k;
		//for (i = 0; i < n; i++) {
		//	for (j = 0; j < n; j++)
		//		printf("%2d ", a[i][j]);
		//	printf("\n");
		//}

		
		for (k = 0; k < n * n; k++) {
			scanf("%d", &a[offi[k]][offj[k]]);
		}
		
		for (n2 = n; n2 <= n * 3; n2++)
			if (chk_all(n2, n)) break;
		
		printf("Case #%d: %d\n", t, n2 * n2 - n * n);
	}
	
	return (0);
} 
