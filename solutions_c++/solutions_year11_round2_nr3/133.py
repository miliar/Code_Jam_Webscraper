#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <cstring>
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

typedef vector<vector<int> > Graph;
Graph g;
vector<vector<bool> > used;
int n;


void outdata() {
}

void solve() {
}

void gran(int v, int p, vector<int>& res)
{
    p = num(g[v], p);
    if (used[v][p]) return ; else used[v][p] = true;
    res.pb(v);
    gran(g[v][(p + 1) % g[v].size()], v, res);
}

bool lessSize(const vector<int>& a, const vector<int>& b) { return a.size() < b.size(); }

typedef vector<int> vi;
typedef vector<vi> vvi;

vi notUsedCols(int numCol, const vvi& grans, const vi& cols, int gNum)
{
   vector<bool> ex(numCol, false);
   const vi& gran = grans[gNum];
   forv(j, gran) if (cols[gran[j]] != -1) ex[cols[gran[j]]] = true;
   vi nex;
   forv(j, ex) if (!ex[j]) nex.pb(j);
   return nex;
}

void readdata() {
    int m;
    cin >> n >> m;
    vector<int> x(m), y(m);
    forn(i, m) {
        cin >> x[i];
		--x[i];
    }
    forn(i, m) {
        cin >> y[i];
		--y[i];
    }
    g.clear();
    g.resize(n);
    forn(i, m) {
        g[x[i]].pb(y[i]);
        g[y[i]].pb(x[i]);
    }
    forn(i, n) {
        g[i].pb((i + 1) % n);
        g[(i + 1) % n].pb(i);
    }

    forn(i, n) sort(all(g[i]));
    used.clear();
    used.resize(n);
    forn(i, n) used[i].resize(g[i].size(), false);
    
    vector<vector<int> > grans;
    forn(i, n) {
        forv(j, g[i]) {
            if (!used[i][j]) {
                vector<int> cg;
                gran(i, g[i][j], cg);
                grans.pb(cg);
            }
        }
    }

    sort(all(grans), lessSize);

    for(int numCol = grans[0].size(); numCol > 0; /*--numCol*/) {
        vector<int> cols(n, -1);

        vector<bool> usG(grans.size(), false);


        bool ok = true;
        forv(_, grans) {
            int bestNum = -1, bestG = -1;
            forv(i, grans) if (!usG[i]) {
                int cc = notUsedCols(numCol, grans, cols, i).size();
                if (bestG == -1 || (bestNum > cc && cc != 0)) {
                    bestG = i;
                    bestNum = cc;
                }
            }
			usG[bestG] = true;
            vi nex = notUsedCols(numCol, grans, cols, bestG);
            nex.pb(0);
            int t = 0;
			vi& gran = grans[bestG];
            random_shuffle(all(gran));
            forv(j, gran) if (cols[gran[j]] == -1) {
                cols[gran[j]] = nex[t++];
                if (t == nex.size()) --t;
            }
            if (t + 1 != nex.size()) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << numCol << endl;
            forv(i, cols) {
                if (i > 0) cout << " ";
                cout << cols[i] + 1;
            }
            cout << endl;
			break;
        } else {
            cerr << ":(" << endl;
        }
    }

}

int main() {
//	freopen(C_IN_FILE, "rt", stdin);

    int t;          
    cin >> t;
    forn(i, t) {
        cerr << i << endl;
        cout << "Case #" << i + 1 << ": ";
    	readdata();
	    solve();
    	outdata();
    }
	return 0;
}

