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
#define all(a) a.begin,a.end()
#define ll long long
#define INF 1e9
#define EPS 1e-8

int nc;
int n, m;
string s[77];
bool used[77][77];

int d[11][11][11][11];

int dx[4] = {1, 0, 0, -1};
int dy[4] = {0, 1, -1, 0};

void dfs(int i, int j) {
	if (i < 0 || j < 0 || i >= n || j >= m || s[i][j] == '#')
		return;
	if (used[i][j])return;
	used[i][j] = 1;
	++nc;
	fore(k, 1, 4) {
		dfs(i + dx[k], j + dy[k]);
	}
}

pii go(int i, int j, int k) {
	pii p = mp(i + dx[k], j + dy[k]);
	if (p.first < 0 || p.second < 0 || p.first >= n || p.second >= m || s[p.first][p.second] == '#')
		return mp(i, j);
	return p;
}

int get(int i, int j, int ii, int jj) {
	int& res = d[i][j][ii][jj];
	if (res > -1)return res;
	if (i == ii && j == jj)
		return res = 1;

	res = 0;
	forn(k, 3) {
		int ni, nj, mi, mj;
		ni = go(i, j, k).first;
		nj = go(i, j, k).second;
		mi = go(ii, jj, k).first;
		mj = go(ii, jj, k).second;
		if (!used[ni][nj] || !used[mi][mj])
			continue;
		if (get(ni, nj, mi, mj) == 1)
			return res = 1;
	}
	return 0;
}

bool okey() {
	forn(i, n) {
		forn(j, m) {
			if (!used[i][j])continue;
			forn(ii, n) {
				forn(jj, m) {
					if (!used[ii][jj])continue;	
					memset(d, -1, sizeof d);
					if (get(i, j, ii, jj) == 0){
						//cerr << i << " " << j << " " << ii << " " << jj << endl;
						return 0;
					}
				}
			}
		}
	}
	return 1;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	
	forn(tt, t){


		cin >> n >> m;
		forn(i, n) 
			cin >> s[i];

		map<char, pii >  res;

		forn(i, n) {
			forn(j, m) {
				if (isdigit(s[i][j])) {
					nc = 0;
					memset(used, 0, sizeof used);
					dfs(i, j);
					memset(d, -1, sizeof d);
					res[s[i][j]] = mp(nc, okey());
				}
			}
		}


		cout << "Case #" << (tt + 1) << ":\n" ;
		for(map<char, pii >::iterator it = res.begin(); it != res.end(); ++it) {
			cout << (*it).first << ": " << (*it).second.first << " " << ((*it).second.second ? "Lucky" : "Unlucky") << endl;
		}
	
	}
	
	return 0;
}