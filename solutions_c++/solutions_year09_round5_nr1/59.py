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
#include <queue>
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

typedef pair<int, int> point;
#define x first
#define y second
typedef vector<point> position;

map<position, int> d;
queue<position> q;

const int NMAX = 15;
int n, m;
bool desk[NMAX][NMAX];
position st, fn;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int ans;

inline bool in(point p) {
    return (0 <= p.x && p.x < n) && (0 <= p.y && p.y < m);
}

bool empty(point& p, position& v) {
    return in(p) && desk[p.x][p.y] && !binary_search(all(v), p);
}

inline bool near(point& a, point& b) {
    return abs(a.x - b.x) + abs(a.y - b.y) == 1;
}

bool connected(position& v) {
    vector<bool> us(v.size());
    us[0] = true;
    queue<int> q;
    q.push(0);
    while (!q.empty()) {
        int i = q.front();
        q.pop();
        forv(j, v) if (!us[j] && near(v[i], v[j])) {
            us[j] = true;
            q.push(j);                        
        }
    }
    forv(i, us) if (!us[i]) {
        return false;
    }
    return true;
}

void outdata() {
    cout << ans << endl;
}

void go(position v) {
    forv(i, v) {
        int nd = d[v] + 1;
        forn(t, 4) {
            point top = point(v[i].x + dx[t], v[i].y + dy[t]);
            point fromp = point(v[i].x - dx[t], v[i].y - dy[t]);
            position nv = v;
            nv[i] = top;
            norm(nv);
            if (empty(top, v) && empty(fromp, v)) {
                if (connected(v) || connected(nv)) {
                    if (d.count(nv) == 0 || d[nv] > nd) {
                        d[nv] = nd;
                        q.push(nv);
                    }
                }
            }
        }
    }    
}

void solve() {
    norm(st);
    norm(fn);
    q.push(st);
    while (!q.empty()) {
        position v = q.front();
        q.pop();
        go(v);
    }
    ans = -1;
    if (d.count(fn)) ans = d[fn];
}

void readdata() {
    d.clear();
    st.clear();
    fn.clear();
    cin >> n >> m;
    forn(i, n) {
        string s;
        cin >> s;
        forn(j, m) {
            char c = s[j];
            if (c == '.') {
                desk[i][j] = true;
            } else if (c == '#') {
                desk[i][j] = false;
            } else if (c == 'x') {
                desk[i][j] = true;
                fn.pb(point(i, j));
            } else if (c == 'o') {
                desk[i][j] = true;
                st.pb(point(i, j));
            } else if (c == 'w') {
                desk[i][j] = true;
                st.pb(point(i, j));
                fn.pb(point(i, j));
            }
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
