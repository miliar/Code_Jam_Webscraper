#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, a) for (int i = 0; i < int(a.size()); i++)
#define fors(i, a) for (int i = 0; i < int(a.length()); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

const int NMAX = 30000;
const int INF = 100000000;

int n, v;
int g[NMAX], a[NMAX], c[NMAX];
int t[NMAX][2];

void outdata() {
	if (t[1][v] == INF) {
		cout << "IMPOSSIBLE";
	} else {
		cout << t[1][v];
	}
	cout << endl;
}

void solve() {
}

void readdata() {
	cin >> n >> v;
	int nleaf = (n - 1) / 2;
	forn(i, nleaf) {
		cin >> g[i + 1] >> c[i + 1];
	}
	for(int i = nleaf + 1; i <= n; ++i) {
		cin >> a[i];
	}
	memset(t, 0, sizeof t);
	forn(i, n + 1) t[i][0] = t[i][1] = INF;
	for(int i = nleaf + 1; i <= n; ++i) {
		t[i][a[i]] = 0;
	}
	for(int i = nleaf; i >= 1; --i) {
		//OR
		int add = (g[i] == 1);
		if (add == 0 || c[i] == 1) {
    		for(int l = 0; l <= 1; ++l) 
    			for(int r = 0; r <= 1; ++r) 
    		        t[i][l | r] = min(t[i][l | r], t[i * 2][l] + t[i * 2 + 1][r] + add);
		}
		//AND
		add = (g[i] == 0);
		if (add == 0 || c[i] == 1) {
			for(int l = 0; l <= 1; ++l) 
				for(int r = 0; r <= 1; ++r) 
		    	    t[i][l & r] = min(t[i][l & r], t[i * 2][l] + t[i * 2 + 1][r] + add);
		}
	}
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		readdata();
		solve();
		outdata();
	}
	return 0;
}
