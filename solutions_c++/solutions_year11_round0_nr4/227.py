#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double
#define PLL pair <ld, ld>
#define PII pair <int, int>
#define pb push_back

const ld EPS = 1e-9;
const int MAXN = 2000;
const int INF = (int)(1e9 + 1e-9);

ld ans[MAXN];
ld C[MAXN][MAXN];
ld fac[MAXN], q[MAXN];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("d.out", "wt", stdout);    
	
	memset(C, 0, sizeof C);
	C[0][0] = 1;

	fore(i, 1, MAXN){
		forn(j, i + 1){
			if (j == 0 || j == i){
				C[i][j] = 1;
				continue;
			}

			C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
		}
	}
	
	fac[0] = 1;
	fore(i, 1, MAXN){
		fac[i] = fac[i - 1] * i;
	}

	q[0] = 1;
	q[1] = 0;

	fore(i, 2, MAXN){
		q[i] = fac[i];
		fore(j, 1, i + 1){
			if (j + 1 == i) continue;
			q[i] -= C[i][j] * q[i - j];
		}
	}

	int tk;
	cin >> tk;

	ans[0] = 0;
	ans[1] = 0;

	fore(i, 2, MAXN){
		ld a = 1, b = 1, t = 0;
		fore(j, 2, i + 1){
			if (j == i) a -= (C[i][i - j] * q[j]) / fac[i];
			else b += (C[i][i - j] * q[j]) / fac[i] * ans[j];
		}


		ans[i] = b / a;
	}
	/*
	fore(i, 2, 11){
		printf("ans[%d] = %.9lf\n", i, ans[i]);
	}
	*/

	fore(i, 20, MAXN){
		ans[i] = i;
	}
	forn(ii, tk){

		int n, cnt = 0;
		cin >> n;
		if (ii == 23){
			ii = ii;
		}
		forn(i, n){
			int x = 0;
			cin >> x;
			if (x != i + 1) ++cnt;
		}

		printf("Case #%d: %.9lf\n", ii + 1, ans[cnt]);
	}

	return 0;
}
