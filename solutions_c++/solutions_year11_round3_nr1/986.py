#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <functional>
using namespace std;
#define pb push_back 
#define mp make_pair
#define sz(v) ((int)(v).size()) 
#define rep(i,n) for(int i=0;i<(n);++i) 
#define all(a) (a).begin(),(a).end()
#define foreach(i, a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define inf (1LL << 29)
typedef long long ll;
typedef vector<int> vi;

int H, W;

bool isPut(int x, int y, vector<string>& mat) {
    if (x + 1 >= W || y + 1 >= H) return false;
    if (mat[y][x] == '.' ||
        mat[y][x+1] == '.' ||
        mat[y+1][x] == '.' ||
        mat[y+1][x+1] == '.') {
        return false;
    }
    mat[y][x] = '/';
    mat[y][x+1] = '\\';
    mat[y+1][x] = '\\';
    mat[y+1][x+1] = '/';
    return true;
}

vector<string> solve() {
    vector<string> imp(1, "Impossible");
    H, W; cin >> H >> W;
    vector<string> mat(H);
    rep(i, H) { cin >> mat[i]; }
    bool ok = false;
    rep(y, H) {
        string& cur = mat[y];
        int cnt = count(all(cur), '#');
        if (cnt % 2 == 1) {
            return imp;
        }
        if (cnt > 0) {
            ok = true;
        }
    }
    if (ok == false) { // all '.'
        return mat;
    }
    bool visited[51][51];
    memset(visited, 0, sizeof(visited));
    rep(y, H) {
        rep(x, W) {
            if (visited[y][x] == true) {
                continue;
            }
            if (mat[y][x] == '#') {
                if (isPut(x, y, mat) == true) {
                    visited[y][x] = true;
                    visited[y][x+1] = true;
                    visited[y+1][x] = true;
                    visited[y+1][x+1] = true;
                }else {
                    return imp;
                }
            }
        }
    }
    rep(y, H) {
        int cnt = count(all(mat[y]), '#');
        if (cnt > 0) return imp;
    }
    return mat;
}

main() {
    ios_base::sync_with_stdio(false);

    int T; cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
        cout << "Case #" << testcase << ":\r\n";
        vector<string> v = solve();
        if (v.size() == 1 && v[0] == "Impossible") {
            cout << "Impossible" << '\r' << endl;
        } else {
            rep(i, sz(v)) {
                cout << v[i] << '\r' << endl;
            }
        }
    }
}
