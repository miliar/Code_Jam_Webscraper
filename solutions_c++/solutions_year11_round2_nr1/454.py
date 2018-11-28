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

#define SZ 128

char a[SZ][SZ];
double w[SZ], g[SZ], wp[SZ], owp[SZ], oowp[SZ], rpi[SZ];

int main() {
	int c, tc;
	scanf("%d", &tc);
	for (c = 1; c <= tc; c++) {
		int i, j, n;
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%s", a[i]);
		for (i = 0; i < n; i++) {
			w[i] = 0, g[i] = 0;
			for (j = 0; j < n; j++) {
				if (a[i][j] != '.') g[i]++;
				if (a[i][j] == '1') w[i]++;
			}
			wp[i] = (double) w[i] / g[i];
		}
		for (i = 0; i < n; i++) {
			int o = 0;
			double s = 0;
			for (j = 0; j < n; j++) {
				if (a[i][j] == '.') continue;
				o++;
				if (a[i][j] == '1')
					s += (double) (w[j] - 0) / (g[j] - 1);
				else
					s += (double) (w[j] - 1) / (g[j] - 1);
			}
			owp[i] = s / o;
		}
		for (i = 0; i < n; i++) {
			int o = 0;
			double s = 0;
			for (j = 0; j < n; j++) {
				if (a[i][j] == '.') continue;
				o++;
				s += owp[j];
			}
			oowp[i] = s / o;
		}
		printf("Case #%d:\n", c);
		for (i = 0; i < n; i++) {
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.9lf\n", rpi[i]);
		}
	}
	
	return (0);
}
