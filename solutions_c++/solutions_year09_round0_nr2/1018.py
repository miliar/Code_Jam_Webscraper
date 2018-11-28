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

int n, m;

int a[111][111];
char res[111][111];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

char last = 'a';

char go(int x, int y) {
    if (res[x][y] != 0) {
        return res[x][y];
    }
    int ps = -1;
    int bst = a[x][y];
    int rx = -1, ry = -1;
    forn(i, 4) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
            if (a[nx][ny] < bst) {
                bst = a[nx][ny];
                ps = i;
                rx = nx;
                ry = ny;
            }
        }
    }
    if (ps == -1) {
        return res[x][y] = last++;
    } else {
        return res[x][y] = go(rx, ry);
    }
}

void outdata() {
}

void solve() {
    forn(i, n) forn(j, m) {
        go(i, j);
    }
    forn(i, n) {
        forn(j, m) {
            if (j > 0) cout << " ";
            cout << res[i][j];
        }
        cout << endl;
    }    
}

void readdata() {
    cin >> n >> m;
    forn(i, n) forn(j, m) {
        cin >> a[i][j];
        res[i][j] = 0;
    }
}

int main() {
    int tst;
    cin >> tst;
    forn(i, tst) {
        cout << "Case #" << i + 1 << ":" << endl;
        last = 'a';
    	readdata();
	    solve();
    	outdata();
    }
	return 0;
}
