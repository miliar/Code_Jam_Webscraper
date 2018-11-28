#pragma comment(linker, "/STACK:64000000")
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
#define x first
#define y second
const ld EPS = 1e-6;
const int MAXN = 1010;
const int INF = (int)(1e9 + 1e-9);
char tmp[MAXN][MAXN];

int p[MAXN], v[MAXN];
int c, d;

bool can(ld x){
	ld t = p[0] - x;

	forn(i, c){
		forn(j, v[i]){
			ld l = p[i] - x, r = p[i] + x;

			if (t + d < r + EPS){
				t = max(t + d, l);
				continue;
			}

			return 0;
			
		}
	}
	return 1;
}
int main()
{
    freopen("input.txt","rt", stdin);
    freopen("b.out", "wt", stdout);    
	int tk;
	cin >> tk;

	cout.precision(9);
	cout.setf(ios::fixed);

	forn(ii, tk){
		ld ans = 0;

		
		cin >> c >> d;

		forn(i, c){
			cin >> p[i] >> v[i];
		}


		ld l = 0, r = (ld)(6e11);

		--v[0];

		if (ii == 8){
			ii = ii;
		}
		forn(iii, 210){
			ld mid = (l + r) / 2;

			if (can(mid)) r = mid;
			else
				l = mid;
		}

		ans = l;

		if (ans > 1e6){
			ans = ans;
		}
		
		printf("Case #%d: %.9Lf\n", ii + 1, ans);

	}
	

	
	return 0;
}
