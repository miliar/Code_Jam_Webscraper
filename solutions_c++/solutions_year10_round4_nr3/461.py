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

const int INF = (int)(1e7 + 1e-7);
const ld EPS = 1e-8;
const int MAXN = 402;

bool a[MAXN][MAXN];
bool b[MAXN][MAXN];

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
	int tk;
	cin >> tk;
	forn(ii, tk){
		int n;
		cin >> n;

		int X = 0, Y = 0;
		memset(a, 0, sizeof a);
		forn(kk, n){
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			X = max(X, y2);
			
			Y = max(Y, x2);
			--x1;
			--x2;
			--y1;
			--y2;
			fore(i, y1, y2 + 1){
				fore(j, x1, x2 + 1){
					a[i][j] = 1;
				}
			}
		}

		int cnt = 0;
		while (true){
			bool f = 0;
/*
			forn(i, 5){
				forn(j, 5){
					cout << int(a[i][j]) << " ";
				}
				cout << endl;
			}
			cout << endl;
*/
			forn(i, X){
				forn(j, Y){
					b[i][j] = a[i][j];

					if (a[i][j]){
						if (i == 0 || a[i - 1][j] == 0){
							if (j == 0 || a[i][j - 1] == 0){
								b[i][j] = 0;
							}
						}
					}

					if (!a[i][j]){
						if (i && a[i - 1][j]){
							if (j && a[i][j - 1]){
								b[i][j] = 1;
							}
						}
					}

					if (b[i][j]){
						f = 1;
						X = max(X, i + 1);
						Y = max(Y, j + 1);
					}
				}
			}

			if (!f) break;
			++cnt;

			forn(i, X){
				forn(j, Y){
					a[i][j] = b[i][j];
				}
			}
		}

		++cnt;
		printf("Case #%d: %d\n", ii + 1, cnt);
	}

     return 0;
}