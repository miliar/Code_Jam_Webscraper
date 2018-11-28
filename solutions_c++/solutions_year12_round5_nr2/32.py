#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>
#include <set>
#include <algorithm>
#include <string>

using namespace std;

typedef pair<int, int> pii;
struct node {
    int x, y;
    bool active;

    node() {
        x = y = active = 0;
    }

    vector<int> ng;
};

bool ok(int x, int y, int S) {
    if (x < 1 || y < 1) return false;
    if (x >= 2*S || y >= 2*S) return false;

    int d = x - y;
    if (d < 0) d = -d;
    if (d > S - 1) return false;

    return true;
}

int dx[] = {1, 1, 0, 0, -1, -1};
int dy[] = {0, 1, -1, 1, -1, 0};

void build(int S, vector<node>& g, vector<pii> have) {
    set<pii> all;

    for (int s = 1; s <= S; s++) {
        have.push_back( make_pair(s, S) );
        have.push_back( make_pair(S, s) );

        have.push_back( make_pair(s, s + S - 1) );
        have.push_back( make_pair(s + S - 1, s) );

        have.push_back( make_pair(s + S - 1, S * 2 - 1) );
        have.push_back( make_pair(S * 2 - 1, s + S - 1) );
    }

    for (int x = 1; x <= 2*S - 1; x++)
        for (int y = 1; y <= 2*S - 1; y++)
            if (ok(x, y, S))
                have.push_back( make_pair(x, y) );

    for (int i = 0; i < (int)have.size(); i++) {
        int x = have[i].first;
        int y = have[i].second;

        all.insert( make_pair(x, y) );
        for (int k = 0; k < 6; k++) {
            int _x, _y;
            _x = x + dx[k];
            _y = y + dy[k];

            if (ok(_x, _y, S)) {
                all.insert( make_pair(_x, _y) );
            }
        }
    }

    g.resize(all.size());
    vector<pii> a(all.begin(), all.end());
    
    for (int i = 0; i < (int)a.size(); ++i) {
        g[i].x = a[i].first;
        g[i].y = a[i].second;

        for (int k = 0; k < 6; k++) {
            int _x, _y;
            _x = g[i].x + dx[k];
            _y = g[i].y + dy[k];

            if (all.count(make_pair(_x, _y))) {
                g[i].ng.push_back(lower_bound(a.begin(), a.end(), make_pair(_x, _y)) - a.begin());
            }
        }
    }
};

void dfs(int id, const vector<node>& g, vector<int>& was, int c, bool active = true) {
   if (was[id]) return;
   was[id] = c;

   for (int i = 0; i < g[id].ng.size(); i++)
   {
       int to = g[id].ng[i];
       if (g[to].active == active) dfs(to, g, was, c, active);
   }
}

int is_corner(int x, int y, int S) {
    if (x == 1 && y == 1) return 1;
    if (x == 1 && y == S) return 2;
    if (x == S && y == 1) return 3;
    if (x == S && y == 2*S - 1) return 4;
    if (x == 2*S-1 && y == S) return 5;
    if (x == 2*S-1 && y == 2*S-1) return 6;

    return 0;
}

int is_edge(int x, int y, int S) {
    if (is_corner(x, y, S) > 0) return 0;
    
    if (x == 1) return 1;
    if (y == 1) return 2;
    if (x == y + S - 1) return 3;
    if (x + S - 1 == y) return 4;
    if (x == S * 2 - 1) return 5;
    if (y == S * 2 - 1) return 6;

    return 0;
}

int count_bit(int x) {
    int res =0 ;
    while (x) {
        res++;
        x &= x - 1;
    }
    return res;
}

void solve() {
    int S, M;
    cin >> S >> M;
    vector<pii> moves(M);

    for (int i = 0; i < M; i++) {
        cin >> moves[i].first >> moves[i].second;
    }

    vector< node > g;
    build(S, g, moves);
    vector<int> was(g.size());

    string res = "-none";

    for (int mi = 0; mi < (int)moves.size(); ++mi) {
        for (int i = 0; i < g.size(); i++)
            if (g[i].x == moves[mi].first && g[i].y == moves[mi].second)
                g[i].active = true;

        was = vector<int>(g.size(), 0);
        
        int comp = 0;
        for (int i = 0; i < g.size(); i++) if (g[i].active && was[i] == 0) {
            comp++;
            dfs(i, g, was, comp);
        }

        comp++;
        for (int i = 0; i < g.size(); i++) if (g[i].active == false && was[i] == 0 &&
            (is_corner(g[i].x, g[i].y, S) || is_edge(g[i].x, g[i].y, S)))
            dfs(i, g, was, comp, false);

        vector<int> corner(comp + 1);
        bool ring(false), corn(false), edg(false);
        vector<int> edge(comp + 1);

        for (int i = 0; i < g.size(); i++) if (g[i].active) {
            int type;
            if ( type = is_corner(g[i].x, g[i].y, S) ) {
                corner[ was[i] ] |= 1 << type;
                corn |= count_bit(corner[ was[i] ]) >= 2;
            }
            if ( type = is_edge(g[i].x, g[i].y, S) ) {
                edge[ was[i] ] |= 1 << type;
                edg |= count_bit(edge[ was[i] ]) >= 3;
            }

        } else {
            if (was[i] == 0) ring = true;
        }

        if (corn || edg || ring) res = "";
        else continue;

        if (corn) res += "-bridge";
        if (edg) res += "-fork";
        if (ring) res += "-ring";

        res += " in move ";
        char s[100];
        sprintf(s, "%d", mi + 1);
        res += s;

        if (corn || edg || ring) break;
    }

    static int test;
    cout << "Case #" << ++test << ": ";
    res = res.substr(1);
    cout << res << endl;     
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
