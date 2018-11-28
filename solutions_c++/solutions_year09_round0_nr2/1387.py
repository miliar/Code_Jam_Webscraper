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

#define N 105

const int dy[4] = {0, -1, 1, 0};
const int dx[4] = {-1, 0, 0, 1};

int a[N][N];
int ans[N][N];
char ansc[30];
int n, m, k;

bool inMap(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < m;
}

int get(int x, int y) {
	if (ans[x][y] != -1) return ans[x][y];

	int mn = INF, ansm;
	forn(i, 4) {
		int tx = x + dx[i], ty = y + dy[i];
		if (!inMap(tx, ty) || a[tx][ty] >= a[x][y]) continue;
		if (a[tx][ty] < mn) {
			mn = a[tx][ty];
			ansm = get(tx, ty);
		}
	}
	if (mn == INF) ans[x][y] = k++;
	else ans[x][y] = ansm;
	return ans[x][y];
}


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d", &tk);
	for(int tc = 1; tc <= tk; ++tc) {
		printf("Case #%d:\n", tc);
		scanf("%d%d", &n, &m);
		forn(i, n)
			forn(j, m) {
				ans[i][j] = -1;
				scanf("%d", &a[i][j]);
			}
		k = 0;
		memset(ansc, 0, sizeof ansc);
		char cur = 'a';
		forn(i, n) {
			forn(j, m) {
				if (ansc[get(i, j)] == 0) {
					ansc[get(i, j)] = cur++;
				}
				printf("%c ", ansc[get(i, j)]);
			}
			printf("\n");
		}
	}
	return 0;
}
