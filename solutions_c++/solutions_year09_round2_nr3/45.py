#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
#include <utility>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double

#define PII pair <int, int>

#define x first
#define y second

const ld EPS = 1e-9;
const int MAXN = 22;
const int MAXQ = MAXN * MAXN;
const int MAXM = 360;

const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

char tmp[MAXN];
string s[MAXM];
int n, m;
int qx[MAXQ], qy[MAXQ];
bool can[MAXN][MAXN][MAXM * 2];
bool us[MAXN][MAXN];
string ans[MAXN][MAXN][MAXM * 2];

bool valid(int x){
	return (x > -1 && x < n);
}

bool valid(int x, int y){
	return valid(x) && valid(y);
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
/*
	forn(i, 10){
		cout << i << "-";
	}
	cout << endl;
	return 0;
*/
	int tk;
	cin >> tk;

	forn(test, tk){
		
		scanf("%d %d", &n, &m);
		
		forn(i, n){
			scanf("%s", &tmp);
			s[i] = tmp;
		}

		int h, t;
		
		memset(can, 0, sizeof can);
		memset(us, 0, sizeof us);
		
		h = 0;
		t = 0;
		forn(i, n){
			forn(j, n){
				if (s[i][j] >= '0' && s[i][j] <= '9'){
					qx[t] = i;
					qy[t] = j;
					can[i][j][s[i][j] - '0' + MAXM] = 1;
					ans[i][j][s[i][j] - '0' + MAXM] = s[i][j];
					us[i][j] = 1;
					++t;
				}
			}
		}

		int x, y;
		int x1, y1;
		int x2, y2;
		int nval, kf;
		int sz;
		string ns;

		while (h != t){
			x = qx[h];
			y = qy[h];
			++h;
			if (h == MAXQ) h = 0;

			us[x][y] = 0;

			forn(k, 4){
				x1 = x + dx[k];
				y1 = y + dy[k];
				if (!valid(x1, y1)) continue;

				kf = 1;
				if (s[x1][y1] == '-') kf = -1;

				forn(k1, 4){
					x2 = x1 + dx[k1];
					y2 = y1 + dy[k1];
					if (!valid(x2, y2)) continue;

					forn(val, 2 * MAXM){
						if (!can[x][y][val]) continue;
						nval = val + kf * (s[x2][y2] - '0');
						if (nval > 2 * MAXM - 1 || nval < 0) continue;

						sz = ans[x][y][val].size() + 2;

						//ns = ans[x][y][val] + s[x1][y1] + s[x2][y2];

						if (!can[x2][y2][nval] || (sz < ans[x2][y2][nval].size()) ||
							(sz == ans[x2][y2][nval].size() && ans[x][y][val] + s[x1][y1] + s[x2][y2] < ans[x2][y2][nval])){
							can[x2][y2][nval] = 1;
							ans[x2][y2][nval] = ans[x][y][val] + s[x1][y1] + s[x2][y2];

							if (!us[x2][y2]){
								us[x2][y2] = 1;
								qx[t] = x2;
								qy[t] = y2;
								++t;
								if (t == MAXQ) t = 0;
							}
						}
					}
				}
			}
		}
		
		printf("Case #%d:\n", test + 1);

		
		forn(iii, m){
			int x;
			scanf("%d", &x);
			x += MAXM;
			ns = "";

			forn(i, n){
				forn(j, n){
					if (can[i][j][x]){
						if (ns == "" || ns.size() > ans[i][j][x].size() || ns.size() == ans[i][j][x].size() &&
							ns > ans[i][j][x]){
							ns = ans[i][j][x];
						}
					}
				}
			}
			printf("%s\n", ns.c_str());
		}
	}

	//cout << clock() << endl;
	return 0;
}