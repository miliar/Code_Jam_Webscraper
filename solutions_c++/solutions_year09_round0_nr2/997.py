#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#pragma comment (linker, "/STACK:99000111")

#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <ctime>
#include <cassert>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)a; i < (int)b; ++i)
#define ford(i, n) for(int i = (int)(n - 1); i >= 0; --i)
#define forv(i, v) for(int i = 0; i < (int)(v.size()); ++i)
#define fs first 
#define sc second
#define mp make_pair
#define pb push_back
#define last(a) a[a.size() - 1]
#define all(a) a.begin(), a.end()
#define norm(a) sort(all(a));a.erase(unique(all(a)), a.end())
#define sz(a) a.size()
#define vi vector<int>
#define pii pair<int,int>

#define INF 1000 * 1000 * 1000
#define EPS 1e-9
#define MAXN 101

using namespace std;

bool u[MAXN][MAXN];

int dx[] = {-1,  0, 0, 1};
int dy[] = { 0, -1, 1, 0};

int n, m, t;

int a[MAXN][MAXN];

vector<pii> g[MAXN][MAXN]; 

char cc[MAXN][MAXN];

void dfs(int i, int j, char ch) {
	cc[i][j] = ch;
	forn(k, g[i][j].size()){
		int a = g[i][j][k].fs, b = g[i][j][k].sc;
		if (cc[a][b] == -1) {
			dfs(a, b, ch);
		}
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cin >> t;
	forn(tt, t) {
		cin >> n >> m;
		forn(i, n)
			forn(j, m){
				scanf("%d", &a[i][j]);
				g[i][j].clear();
		}
		forn(i, n)
			forn(j, m){
				int b = -1;
				int mn = INF;
				int ii , jj;
				forn(d, 4){
					if (i + dx[d] >= 0 && j + dy[d] >= 0 && i + dx[d] < n && j + dy[d] < m) {
						if (a[i + dx[d]][j + dy[d]] < a[i][j] && a[i + dx[d]][j + dy[d]] < mn){
							mn = a[i + dx[d]][j + dy[d]];
							b = d;
							ii = i + dx[d];
							jj = j + dy[d];
						}
					}
				}
				if (b > -1){
					g[ii][jj].pb(mp(i, j));
					g[i][j].pb(mp(ii, jj));
				}
		}
		char c = 'a';
		memset(cc, -1, sizeof cc);
		forn(i, n){
			forn(j, m)
				if (cc[i][j] == -1){
					dfs(i, j, c);
					c++;	
				}
		}
		printf("Case #%d:\n", tt + 1);
		forn(i, n){
			forn(j, m)
				printf("%c ", cc[i][j]);
			puts("");
		}

	}
	return 0;
}