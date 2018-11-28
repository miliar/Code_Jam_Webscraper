#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>

#include <cassert>
#include <cmath>
#include <ctime>

#include <map>
#include <set>
#include <bitset>
#include <queue>

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()

const int INF = INT_MAX >> 1;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1E-8;

#define N 10

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};

int n, m;

bool inMap(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < n;
}


char f[N][N + 1];

map<int, string> d[N][N], d1[N][N];

string ans[100];
int a[100];


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d", &tk);

	for(int tc = 1; tc <= tk; ++tc) {
		printf("Case #%d:\n", tc);

		scanf("%d %d\n", &n, &m);
		forn(i, n) {
			gets(f[i]);
		}

		forn(i, m) {
			scanf("%d", &a[i]);
			ans[i] = string(1, 127);
		}

		forn(i, n)
			forn(j, n)
				d[i][j].clear();

		forn(i, n)
			forn(j, n)
				if (isdigit(f[i][j]))
					d[i][j][f[i][j] - '0'] = string(1, f[i][j]);

		while (true) {
			bool all = true;
			forn(k, m)
				if (ans[k][0] == 127)  {
					forn(i, n)
						forn(j, n)
							if (isdigit(f[i][j]) && d[i][j].count(a[k]))
								ans[k] = min(ans[k], d[i][j][a[k]]);
					if (ans[k][0] == 127) all = false;
				}

			if (all) break;

			forn(i, n)
				forn(j, n)
					d1[i][j].clear();

			forn(i, n)
				forn(j, n)
					if (isdigit(f[i][j]))
						forn(i1, 4) {
							int tx1 = i + dx[i1], ty1 = j + dy[i1];
							if (!inMap(tx1, ty1)) continue;

							forn(i2, 4) {
								int tx2 = tx1 + dx[i2], ty2 = ty1 + dy[i2];
								if (!inMap(tx2, ty2)) continue;

								string ds = string(2, f[tx1][ty1]);
								ds[1] = f[tx2][ty2];
								int dx = (f[tx1][ty1] == '+' ? f[tx2][ty2] - '0' : -(f[tx2][ty2] - '0'));

								for(map<int, string>::iterator it = d[i][j].begin(); it != d[i][j].end(); ++it) {
									int key = it->first + dx;
									string value = it->second + ds;
									string &has = d1[tx2][ty2][key];
									if (has == "" || has > value) has = value;
								}

							}
						}
			forn(i, n)
				forn(j, n)
					d[i][j] = d1[i][j];
		}

		forn(k, m)
			cout << ans[k] << endl;

	}

	return 0;
}
