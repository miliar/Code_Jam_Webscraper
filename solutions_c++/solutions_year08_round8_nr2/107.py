#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
#include <vector>
#include <map>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)

#define ll long long 
#define ld long double

const int MAXN = 310;
const int MAXA = 10100;

const ld EPS = 1e-9;

bool a[MAXA][MAXN];
map <string, int> mp;
int b[MAXA][MAXN];

char tmp[MAXN];
string s;
int x[MAXN], y[MAXN], c[MAXN];

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int tk, n;
	cin >> tk;

	forn(ii, tk){
		mp.clear();
		scanf("%d", &n);
		
		int h = 0;

		forn(i, n){
			scanf("%s", &tmp);
			s = tmp;
			c[i] = mp[s] - 1;

			if (c[i] == -1){
				++h;
				mp[s] = h;
				c[i] = mp[s] - 1;
			}
			
			scanf("%d %d", &x[i], &y[i]);
			--x[i];
			--y[i];
		}
/*		
		forn(i, MAXA){
			forn(j, h){
				b[i][j] = -1;
			}
		}
*/
		memset(b, 255, sizeof b);

		forn(i, n){
			b[x[i]][c[i]] = max(b[x[i]][c[i]], y[i]);
		}

		forn(j, MAXA - 1){
			forn(i, h){
				b[j + 1][i] = max(b[j + 1][i], b[j][i]);
			}
		}

		int ans = n + 1;

		forn(c1, h){
			fore(c2, c1, h){
				int t, q, cur;

				fore(c3, c2, h){
					t = 0;
					cur = 0;
					
					while (true){
						q = max(b[t][c1], max(b[t][c2], b[t][c3]));
						if (q < t) break;

						++cur;
						t = q + 1;
					}

					if (t >= 10000){
						ans = min(ans, cur);
					}
				}
			}
		}

		if (ans > n){
			printf("Case #%d: IMPOSSIBLE\n", ii + 1);
		}
		else
			printf("Case #%d: %d\n", ii + 1, ans);

	}

	return 0;
};