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
#define ld ll
#define PLL pair <ld, ld>
#define PII pair <int, int>
#define pb push_back

const ld EPS = 1e-9;
const int MAXN = 600;
const int INF = (int)(1e9 + 1e-9);

int n;
char tmp[MAXN][MAXN];
ld mas[MAXN][MAXN];

ld l[MAXN][MAXN], r[MAXN][MAXN];
ld l1[MAXN][MAXN], r1[MAXN][MAXN];
ld l2[MAXN][MAXN], r2[MAXN][MAXN];

bool behind(ld x, ld l, ld r){
	return (l < x + EPS && x < r + EPS);
}


void inc(ll &M, ll &X, ll &Y, int i, int j){
	M += mas[i][j];
	X += mas[i][j] * (2 * i + 1);
	Y += mas[i][j] * (2 * j + 1);
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
		int n, m, d;
		cin >> n >> m >> d;

		forn(i, n){
			scanf("%s", &tmp[i]);

			forn(j, m){
				mas[i][j] = (tmp[i][j] - '0') + d;
			}
		}
		
		forn(i, n){
			l[i][0] = 0;
			l1[i][0] = 0;
			l2[i][0] = 0;

			forn(j, m){
				l[i][j + 1] = l[i][j] + mas[i][j];
				l1[i][j + 1] = l1[i][j] + mas[i][j] * (ld)(2 * i + 1);
				l2[i][j + 1] = l2[i][j] + mas[i][j] * (ld)(2 * j + 1);
			}
		}

		forn(j, m){
			r[j][0] = 0;
			r1[j][0] = 0;
			r2[j][0] = 0;

			forn(i, n){
				r[j][i + 1] = r[j][i] + mas[i][j];
				r1[j][i + 1] = r1[j][i] + mas[i][j] * (ld)(2 * i + 1);
				r2[j][i + 1] = r2[j][i] + mas[i][j] * (ld)(2 * j + 1);
			}
		}

		int ans = 1;

		forn(c1, n){
			forn(c2, m){
				ld M = 0, X = 0, Y = 0;

				int L = min(min(c1, c2), min(n - c1 - 1, m - c2 - 1));

				fore(i, 1, L + 1){
					M += r[c2 - i][c1 + i] - r[c2 - i][c1 - i + 1];
					X += r1[c2 - i][c1 + i] - r1[c2 - i][c1 - i + 1];
					Y += r2[c2 - i][c1 + i] - r2[c2 - i][c1 - i + 1];

					M += r[c2 + i][c1 + i] - r[c2 + i][c1 - i + 1];
					X += r1[c2 + i][c1 + i] - r1[c2 + i][c1 - i + 1];
					Y += r2[c2 + i][c1 + i] - r2[c2 + i][c1 - i + 1];

					M += l[c1 - i][c2 + i] - l[c1 - i][c2 - i + 1];
					X += l1[c1 - i][c2 + i] - l1[c1 - i][c2 - i + 1];
					Y += l2[c1 - i][c2 + i] - l2[c1 - i][c2 - i + 1];

					M += l[c1 + i][c2 + i] - l[c1 + i][c2 - i + 1];
					X += l1[c1 + i][c2 + i] - l1[c1 + i][c2 - i + 1];
					Y += l2[c1 + i][c2 + i] - l2[c1 + i][c2 - i + 1];
					
					
					if (X == M * (2 * c1 + 1) && Y == M * (2 * c2 + 1)){
						ans = max(ans, 1 + 2 * i);
					}

					inc(M, X, Y, c1 - i, c2 - i);
					inc(M, X, Y, c1 - i, c2 + i);
					inc(M, X, Y, c1 + i, c2 - i);
					inc(M, X, Y, c1 + i, c2 + i);
				}
			}
		}
		
		forn(c1, n){
			forn(c2, m){
				ld M = 0, X = 0, Y = 0;

				int L = min(min(c1, c2), min(n - c1, m - c2));

				fore(i, 1, L + 1){
					M += r[c2 - i][c1 + i - 1] - r[c2 - i][c1 - i + 1];
					X += r1[c2 - i][c1 + i - 1] - r1[c2 - i][c1 - i + 1];
					Y += r2[c2 - i][c1 + i - 1] - r2[c2 - i][c1 - i + 1];

					M += r[c2 + i - 1][c1 + i - 1] - r[c2 + i - 1][c1 - i + 1];
					X += r1[c2 + i - 1][c1 + i - 1] - r1[c2 + i - 1][c1 - i + 1];
					Y += r2[c2 + i - 1][c1 + i - 1] - r2[c2 + i - 1][c1 - i + 1];

					M += l[c1 - i][c2 + i - 1] - l[c1 - i][c2 - i + 1];
					X += l1[c1 - i][c2 + i - 1] - l1[c1 - i][c2 - i + 1];
					Y += l2[c1 - i][c2 + i - 1] - l2[c1 - i][c2 - i + 1];

					M += l[c1 + i - 1][c2 + i - 1] - l[c1 + i - 1][c2 - i + 1];
					X += l1[c1 + i - 1][c2 + i - 1] - l1[c1 + i - 1][c2 - i + 1];
					Y += l2[c1 + i - 1][c2 + i - 1] - l2[c1 + i - 1][c2 - i + 1];
					
					
					if (X == M * (2 * c1) && Y == M * (2 * c2)){
						if (i > 1)
							ans = max(ans, 2 * i);
					}

					inc(M, X, Y, c1 - i, c2 - i);
					inc(M, X, Y, c1 - i, c2 + i - 1);
					inc(M, X, Y, c1 + i - 1, c2 - i);
					inc(M, X, Y, c1 + i - 1, c2 + i - 1);
				}
			}
		}

		if (ans < 3){
			printf("Case #%d: IMPOSSIBLE\n", ii + 1);
		}
		else
			printf("Case #%d: %d\n", ii + 1, ans);
	}

	return 0;
}

