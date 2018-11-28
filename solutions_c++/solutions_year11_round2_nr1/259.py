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
const ld EPS = 1e-9;
const int MAXN = 210;
const int INF = (int)(1e9 + 1e-9);
char tmp[MAXN][MAXN];

ld a[MAXN], b[MAXN], c[MAXN];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("a.out", "wt", stdout);    
	int tk;
	cin >> tk;

	cout.precision(9);
	cout.setf(ios::fixed);

	forn(ii, tk){
		int n;
		cin >> n;

		forn(i, n){
			scanf("%s", &tmp[i]);
		}

		memset(a, 0, sizeof a);
		memset(b, 0, sizeof b);
		memset(c, 0, sizeof c);

		forn(i, n){
			int cc = 0;
			forn(j, n){
				if (tmp[i][j] == '.') continue;
				++cc;
				if (tmp[i][j] == '1'){
					a[i] = a[i] + 1;
				}
			}

			a[i] /= cc;
		}



		forn(i, n){
			ld q = 0;
			forn(j, n){
				if (tmp[i][j] == '.') continue;
				++q;
				int cc = 0;
				ld t = 0;
				forn(k, n){
					if (i == k) continue;
					if (tmp[j][k] == '.') continue;
					++cc;
					if (tmp[j][k] == '1') 
						t = t + 1;
				}
				b[i] += t / cc;
			}

			b[i] /= q;
		}

		forn(i, n){
			int cc = 0;
			forn(j, n){
				if (tmp[i][j] == '.') continue;
				++cc;
				c[i] = c[i] + b[j];
			}

			c[i] /= cc;
		}

		printf("Case #%d:\n", ii + 1);

		forn(i, n){
			ld t = 0.25 * a[i] + 0.5 * b[i] + 0.25 * c[i];
			cout << t << endl;		
		}
	}
	

	/*
	  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
WP, OWP, and OOWP are defined for each team as follows:
WP (Winning Percentage) is the fraction of your games that you have won.
In the example schedule, team A has WP = 1, team B has WP = 0, team C has WP = 2/3, and team D has WP = 0.5.
OWP (Opponents' Winning Percentage) is the average WP of all your opponents, after first throwing out the games they played against you.
For example, if you throw out games played against team D, then team B has WP = 0 and team C has WP = 0.5. Therefore team D has OWP = 0.5 * (0 + 0.5) = 0.25. Similarly, team A has OWP = 0.5, team B has OWP = 0.5, and team C has OWP = 2/3.
OOWP (Opponents' Opponents' Winning Percentage) is the average OWP of all your opponents. OWP is exactly the number computed in the previous step.
For example, team A has OOWP = 0.5 * (0.5 + 2/3) = 7/12.
Putting it all together, we see team A has RPI = (0.25 * 1) + (0.5 * 0.5) + (0.25 * 7 / 12) = 0.6458333...
	*/
	return 0;
}
