#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#define _CRT_SECURE_NO_DEPRECATE
using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double

#define PLL pair <ld, ld>

#define x first
#define y second

const int MAXN = 4000;
const ld EPS = 1e-9;

int mask[10];

int x[MAXN], y[MAXN], r[MAXN];

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
	
	int tk;
	cin >> tk;

	forn(test, tk){
		int n;
		cin >> n;

		forn(i, n){
			cin >> x[i] >> y[i] >> r[i];
		}


		ld ans = 1e18;

		if (n == 1){
			ans = r[0];
		}
		if (n == 2){
			ans = max(r[0], r[1]);
		}

		if (n == 3){
			forn(i, n){
				PLL c1 = PLL(x[i], y[i]);
				ld cur = r[i];
				vector <PLL> v;
				vector <ld> R;

				forn(j, n){
					if (i == j) continue;
					v.push_back(PLL(x[j], y[j]));
					R.push_back(r[j]);
				}

				PLL p1 = v[0], p2 = v[1];
				ld r1 = R[0], r2 = R[1];

				ld l = hypot(p1.x - p2.x, p1.y - p2.y);

//				ld t1 = (l + r2 - r1) / 2, t2 = (l + r1 - r2) / 2;

//				PLL c2 = PLL(p1.x * t2 + p2.x * t1, p1.y * t2 + p2.y * t1);

				cur = max(cur, (l + r1 + r2) / 2);
				ans = min(ans, cur);
			}
		}

		printf("Case #%d: %.9lf\n", test + 1, ans);
	}


	return 0;
};