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

#define EPS 1e-7

#define SZ 512

char md[SZ][SZ];
double m[SZ][SZ];
double mx[SZ][SZ];
double my[SZ][SZ];
double ma[SZ][SZ];
double mxa[SZ][SZ];
double mya[SZ][SZ];

int main() {
	int cc, C;
	scanf("%d", &C);
	for (cc = 1; cc <= C; cc++) {
		int i, j, l, r, c, d;
		scanf("%d %d %d", &r, &c, &d);
		for (i = 1; i <= r; i++)
			scanf("%s", &md[i][1]);
		for (i = 1; i <= r; i++) {
			for (j = 1; j <= c; j++) {
				m[i][j] = d + md[i][j] - '0';
				mx[i][j] = m[i][j] * j;
				my[i][j] = m[i][j] * i;
			}
		}
		
		for (i = 1; i <= r; i++) {
			for (j = 1; j <= c; j++) {
				ma[i][j] = ma[i][j-1] + ma[i-1][j] - ma[i-1][j-1] + m[i][j];
				mxa[i][j] = mxa[i][j-1] + mxa[i-1][j] - mxa[i-1][j-1] + mx[i][j];
				mya[i][j] = mya[i][j-1] + mya[i-1][j] - mya[i-1][j-1] + my[i][j];
			}
		}
		double smx, smy, sm, cx, cy, l2;
		for (l = min(r, c); l >= 3; l--) {
			for (i = l; i <= r; i++) {
				for (j = l; j <= c; j++) {
					sm = ma[i][j] - ma[i][j-l] - ma[i-l][j] + ma[i-l][j-l];
					smx = mxa[i][j] - mxa[i][j-l] - mxa[i-l][j] + mxa[i-l][j-l];
					smy = mya[i][j] - mya[i][j-l] - mya[i-l][j] + mya[i-l][j-l];
					sm -= m[i][j] + m[i][j-l+1] + m[i-l+1][j] + m[i-l+1][j-l+1];
					smx -= mx[i][j] + mx[i][j-l+1] + mx[i-l+1][j] + mx[i-l+1][j-l+1];
					smy -= my[i][j] + my[i][j-l+1] + my[i-l+1][j] + my[i-l+1][j-l+1];
					cx = smx / sm;
					cy = smy / sm;
					l2 = (l - 1) / 2.0;
					if (fabs(j - l2 - cx) <= EPS && fabs(i - l2 - cy) <= EPS) break;
				}
				if (j <= c) break;
			}
			if (i <= r) break;
		}
		if (l >= 3)
			printf("Case #%d: %d\n", cc, l);
		else
			printf("Case #%d: IMPOSSIBLE\n", cc);
	}
	return (0);
}
