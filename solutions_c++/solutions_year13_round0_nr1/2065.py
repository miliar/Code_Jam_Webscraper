#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <memory>
#include <cassert>
#include <climits>
using namespace std;

#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define ALL(a) (a).begin(), (a).end()

#define DBG(x) cout << #x << " = " << x << endl
// #define DBG(x) ;

const string XWON = "X won";
const string YWON = "O won";
const string DRAW = "Draw";
const string IN_PROGRESS = "Game has not completed";

template<typename T>
void dbg_vector(const vector<T>& v, const string& name) {
    cout << name << " = ";
    REP(i, SIZE(v)) {
        cout << v[i] << ' ';
    }
    cout << endl;
}

bool in(char c, const set<char>& sc) {
    return sc.find(c) != sc.end();
}

bool won(const set<char>& sc, string& res) {
    /*
    vector<char> vc(ALL(sc));
    string s = "";
    REP(i, SIZE(vc)) s += vc[i];
    DBG(s);
    */

    if (sc.size() > 2) return false;
    if (in('.', sc)) return false;
    if (in('X', sc) && in('O', sc)) return false;
    if (in('X', sc)) { res = XWON; return true; }
    if (in('O', sc)) { res = YWON; return true; }
    assert(false);
    return true;
}

string doit(vector<string>& v) {
    string res;
    set<char> sc;
    REP(i, 4) {
        sc.clear();
        REP(j, 4) sc.insert(v[i][j]);
        if (won(sc, res)) return res;
        sc.clear();
        REP(j, 4) sc.insert(v[j][i]);
        if (won(sc, res)) return res;
    }
    sc.clear();
    REP(i, 4) sc.insert(v[i][i]);
    if (won(sc, res)) return res;
    sc.clear();
    REP(i, 4) sc.insert(v[i][3 - i]);
    if (won(sc, res)) return res;
    REP(i, 4) REP(j, 4) if (v[i][j] == '.') return IN_PROGRESS;
    return DRAW;
}

int main() {
    int tests;
    cin >> tests;
    REP(zzz, tests) {
        vector<string> vs(4);
        REP(i, 4) cin >> vs[i];
        // dbg_vector<string>(vs, "vs");
        cout << "Case #" << zzz + 1 << ": " << doit(vs) << endl;
    }

    return 0;
}
