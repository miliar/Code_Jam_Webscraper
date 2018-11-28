#define _CRT_SECURE_NO_DEPRECATE
#define _ASSERTE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define ll long long
#define ld long double
#define INF 1e9
#define EPS 1e-8

int tt, m, s;
int used[101][101];

int dx[6] = {-1, 0, 1, 1, 0, -1};
int dy[6] = {-1, -1, 0, 1, 1, 0};

int n, uc;

bool in (int x, int y) {
	return x >= 1 && y >= 1 && x <= n && y <= n && abs(x - y) <= s - 1;
}

bool corner(int x, int y) {
	return (x == 1 && y == 1) ||
		   (x == 1 && y == s) ||
		   (x == s && y == 1) ||
		   (x == s && y == n) ||
		   (x == n && y == s) ||
		   (x == n && y == n);
}

int edge(int x, int y) {
	if(x == 1 && y > 1 && y < s) return 1;
	if(y == 1 && x > 1 && x < s) return 2;
	if(y == n && x > s && x < n) return 3;
	if(x == n && y > s && y < n) return 4;
	
	if ((x - y == s - 1) && !corner(x, y))
		return 5;
	if ((y - x == s - 1) && !corner(x, y))
		return 6;
	return 0;
}

int us[101][101];

void dfs1(int x, int y) {
	us[x][y] = 1;
	forn(i, 6) {
		int xx = x + dx[i];
		int yy = y + dy[i];
		if (in(xx, yy) && used[xx][yy] == uc && !us[xx][yy]) 
			dfs1(xx, yy);
	}
}

vector<pii> corners;
vector<pii> edges[6];

bool can(int x, int y) {
	if (!in(x, y) || used[x][y] == uc)
		return 0;
	if (us[x][y])
		return us[x][y]==1;
	if (corner(x, y) || edge(x, y))
		return 1;
	us[x][y] = -1;
	forn(i, 6) {
		int xx = x + dx[i];
		int yy = y + dy[i];
		if (can(xx, yy)) {
			us[x][y] = 1;
			return 1;
		}
	}
	return 0;
}

int took;

void dfs2(int x, int y) {
	if (x < 0 || x > n + 1 || y < 0 || y > n + 1)
		return;
	if (us[x][y] || used[x][y] == uc)
		return;
	++took;
	us[x][y] = 1;
	forn(i, 6) {
		int xx = x + dx[i];
		int yy = y + dy[i];
		dfs2(xx, yy);
	}
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	cin >> tt;
	forn(t, tt) {
		cerr << t + 1 << endl;



		uc = t + 1;
		cin >> s >> m;
		n = s * 2 - 1;
		corners.clear();
		forn(i, 6)
			edges[i].clear();
		fore(i, 1, n + 1) {
			fore(j, 1, n + 1){
				if (corner(i, j)) {
					corners.pb(mp(i, j));
				}
				if (edge(i, j)) {
					int e = edge(i, j) - 1;
					edges[e].pb(mp(i, j));
				}
			}
		}

		cout << "Case #" << (t + 1) << ": ";
		bool ready = 0;
		forn(ii, m) {

			int x, y;
			cin >> x >> y;
			if (ready)continue;
			used[x][y] = uc;
			memset(us, 0, sizeof us);
			dfs1(x, y);

			//
			bool bridge = 0;
			int it = 0;
			forn(i, corners.size()){
				if (us[corners[i].first][corners[i].second])
					++it;
			}
			if (it > 1)
				bridge = 1;

			//
			bool edger = 0;
			bool us_edge[6];
			it = 0;
			memset(us_edge, 0, sizeof us_edge);
			forn(i, 6) {
				forn(j, edges[i].size())
					us_edge[i] |= (us[edges[i][j].first][edges[i][j].second] != 0);
				if (us_edge[i])++it;
			}
			if (it > 2)
				edger = 1;

			//
			bool circle = 0;

			took = 0;
			memset(us, 0, sizeof us);
			dfs2(0, 0);
			if (took + ii + 1 != (n + 2) * (n + 2))
				circle = 1;

			if (bridge) {
				ready = 1;
				if (edger){
					if (circle)
						printf("bridge-fork-ring in move %d\n", ii + 1);
					else
						printf("bridge-fork in move %d\n", ii + 1);
				}else{
					if (circle)
						printf("bridge-ring in move %d\n", ii + 1);
					else
						printf("bridge in move %d\n", ii + 1);
				}
			}else{
				if (edger){
					ready = 1;
					if (circle)
						printf("fork-ring in move %d\n", ii + 1);
					else
						printf("fork in move %d\n", ii + 1);
				}else{
					if (circle) {
						printf("ring in move %d\n", ii + 1);
						ready = 1;
					}
				}
			}

		}
		if (!ready)
			puts("none");
	}
	
	
	return 0;
}