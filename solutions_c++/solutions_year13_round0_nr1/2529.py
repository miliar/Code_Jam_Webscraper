#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <complex>
#include <list>
#include <deque>
#include <cassert>
#include <ctime>
using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const double PI = acos(-1.0); 
const double eps = 1e-12;
const int INF = (1 << 31) - 1;
const ll LLINF = ((ll)1 << 62) - 1;

#define mp make_pair
#define pb push_back
#define sz(x) (int)x.size()
#define X first
#define Y second
#define all(x) x.begin(),x.end()
#define fill(a, x) memset(a, x, sizeof(a));
#define next nexttt
#define prev prevvv
#define y1 y111

char a[5][5];

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int n;
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 4; j++) {
			string s;
			cin >> s;
			for (int l = 0; l < sz(s); l++) {
				a[j][l] = s[l];
			}
		}
		printf("Case #%d: ", i + 1);
		bool flag = true, endd = false;
		for (int j = 0; j < n; j++) {
			int c1 = 0, c2 = 0, c3 = 0, c4 = 0, c5 = 0, c6 = 0, c7 = 0, c8 = 0, c9 = 0, c10 = 0, c11 = 0, c12 = 0;
			int kk = 3;
			for (int k = 0; k < 4; k++, kk--) {
				if (a[j][k] == 'O') c1++;
				if (a[j][k] == 'X') c2++;
				if (a[j][k] == 'T') c3++;
				
				if (a[k][j] == 'O') c4++;
				if (a[k][j] == 'X') c5++;
				if (a[k][j] == 'T') c6++;
				
				if (a[k][k] == 'O') c7++;
				if (a[k][k] == 'X') c8++;
				if (a[k][k] == 'T') c9++;

				if (a[k][kk] == 'O') c10++;
				if (a[k][kk] == 'X') c11++;
				if (a[k][kk] == 'T') c12++;

				if (a[j][k] == '.') flag = false;
			}
			if ((c1 == 3 && c3) || (c1 == 4)) {
				puts("O won");
				endd = true;
				break;
			}
			if ((c2 == 3 && c3) || (c2 == 4)) {
				puts("X won");
				endd = true;
				break;
			}
			if ((c4 == 3 && c6) || (c4 == 4)) {
				puts("O won");
				endd = true;
				break;
			}
			if ((c5 == 3 && c6) || (c5 == 4)) {
				puts("X won");
				endd = true;
				break;
			}
			if ((c7 == 3 && c9) || (c7 == 4)) {
				puts("O won");
				endd = true;
				break;
			}
			if ((c8 == 3 && c9) || (c8 == 4)) {
				puts("X won");
				endd = true;
				break;
			}

			if ((c10 == 3 && c12) || (c10 == 4)) {
				puts("O won");
				endd = true;
				break;
			}
			if ((c11 == 3 && c12) || (c11 == 4)) {
				puts("X won");
				endd = true;
				break;
			}
		}
		if (!endd) {
			if (!flag) {
				puts("Game has not completed");
			} else {
				puts("Draw");
			}
		}
	}

	return 0;
}