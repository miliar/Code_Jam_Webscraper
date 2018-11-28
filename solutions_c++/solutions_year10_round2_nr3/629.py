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

const ld EPS = 1e-9;
const int MAXN = 510;
const ll BASE = 100003;

ll a[MAXN][MAXN], c[MAXN][MAXN];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    
	int tk;
	cin >> tk;

	c[0][0] = 1 % BASE;

	forn(i, MAXN){
		forn(j, i + 1){
			if (j == 0 || j == i){
				c[i][j] = 1 % BASE;		
				continue;
			}

			c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % BASE;

		}
	}

	forn(i, MAXN){
		forn(j, MAXN){
			a[i][j] = 0;
		}
	}

	fore(i, 2, MAXN + 1){
		a[i][1] = 1;
	}

	fore(j, 1, MAXN){
		fore(i, j + 1, MAXN){
			fore(k, 2 * i - j, MAXN){
				a[k][i] += a[i][j] * c[k - i - 1][i - j - 1];
				if (k == 4 && i == 2){
					k = k;
				}
				if (a[k][i] > BASE - 1){
					a[k][i] %= BASE;
				}
			}
		}
	}

	forn(ii, tk){
		ll ans = 0;

		int n;
		cin >> n;
		
		forn(i, n + 1){
			ans = (ans + a[n][i]) % BASE; 
		}

		int qans = ans;
		printf("Case #%d: %d\n", ii + 1, qans);
	}
          
    return 0;
}

