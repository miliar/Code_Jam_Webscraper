#pragma comment(linker, "/STACK:50000000")
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#include <memory.h>


using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double
#define PII pair <int, int>
#define PLL pair <ld, ld>

const int INF = (int)(1e9 + 1e-9);
const ld EPS = 1e-8;

const int MAXN = 16;
const int MAXM = 1200;

int a[MAXN][MAXM];
int c[MAXN][MAXM];
int M[MAXM];

ll b[MAXN][MAXM][MAXN];
int mask[20];

void up(ll &a, ll b){
	a = min(a, b);
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

	mask[0] = 1;
	forn(i, 11){
		mask[i + 1] = mask[i] * 2;
	}

	int tk;
	cin >> tk;

	forn(ii, tk){
		int n;
		cin >> n;

		forn(i, mask[n]){
			cin >> M[i];
			M[i] = n - M[i];
		}

		forn(i, n){
			forn(j, mask[n - i - 1]){
				scanf("%d", &a[i][j]);
			}
		}

		forn(j, mask[n - 1]){
			c[0][j] = max(M[2 * j], M[2 * j + 1]);
		}

		fore(i, 1, n){
			forn(j, mask[n - i - 1]){
				c[i][j] = max(c[i - 1][2 * j], c[i - 1][2 * j + 1]);
			}
		}
		
		forn(i, n){
			forn(j, mask[n - i - 1]){
				forn(k, n + 2){
					b[i][j][k] = INF;

					forn(t, 2){
						ll cost = 0;
						if (t) cost = a[i][j];
						
						if (i){
							up(b[i][j][k], cost + b[i - 1][2 * j][k + t] + b[i - 1][2 * j + 1][k + t]); 
						}
						else
							if (k + t >= c[i][j]){
								up(b[i][j][k], cost);
							}
					}
					
				}
			}
		}
		
		ll ans = b[n - 1][0][0];

		printf("Case #%d: %lld\n", ii + 1, ans);
	}

     return 0;
}