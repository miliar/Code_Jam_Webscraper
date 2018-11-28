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
		int i1 = 0, i2 = 0;
		int p1 = 1, p2 = 1;
		vector<pii> v1, v2;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			char r; int p;
			scanf(" %c %d", &r, &p);
			if (r == 'O') v1.push_back(pii(i, p));
			if (r == 'B') v2.push_back(pii(i, p));
		}
		int k = 0;
		while (i1 < (int) v1.size() || i2 < (int) v2.size()) {
			if (i1 < (int) v1.size() && (i2 >= (int) v2.size() || v1[i1].first < v2[i2].first)) {
				while (p1 != v1[i1].second) {
					if (i2 < (int) v2.size() && p2 != v2[i2].second) p2 += (p2 < v2[i2].second) ? +1 : -1;
					p1 += (p1 < v1[i1].second) ? +1 : -1;
					k++;
				}
				{
					if (i2 < (int) v2.size() && p2 != v2[i2].second) p2 += (p2 < v2[i2].second) ? +1 : -1;
					k++;
				}
				i1++;
			}
			else {
				while (p2 != v2[i2].second) {
					if (i1 < (int) v1.size() && p1 != v1[i1].second) p1 += (p1 < v1[i1].second) ? +1 : -1;
					p2 += (p2 < v2[i2].second) ? +1 : -1;
					k++;
				}
				{
					if (i1 < (int) v1.size() && p1 != v1[i1].second) p1 += (p1 < v1[i1].second) ? +1 : -1;
					k++;
				}
				i2++;
			}
		}
		printf("Case #%d: %d\n", c, k);
	}
	
	return (0);
}
