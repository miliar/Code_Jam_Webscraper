#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

const int R = 50;
const int C = 50;
const int INF = 100000;

char m[R][C+1];
int r, c, f;

bool known[R][C][C][2][2];
int dp[R][C][C][2][2];

inline bool canDig(int rr, int cc) {
    if (rr < 0 || rr >= r) return false;
    if (cc < 0 || cc >= c) return false;
    if (m[rr][cc] != '.') return false;
    if (rr+1 >= r) return false;
    if (m[rr+1][cc] == '.') return false;
    return true;
}

void getPlatform(int& rr, int cc, int& a, int& b, int& lo, int& ro) {
    a = -1, b = -1;
    lo = ro = 0;

    if (cc < 0 || cc >= c) return;

    if (rr+1 < r && m[rr+1][cc] == '.') {
        int bottom = rr+1;
        while (bottom < r && m[bottom][cc] == '.') bottom++;
        if (bottom-1 - rr > f) return;
        rr = bottom-1;
        getPlatform(rr, cc, a, b, lo, ro);
        return;
    }

    a = cc-1;
    b = cc+1;
    while (a >= 0 && m[rr][a] == '.' && (rr+1 == r || m[rr+1][a] == '#')) a--;
    a++;
    if (a-1 >= 0 && m[rr][a-1] == '.') lo = 1;

    while (b < c && m[rr][b] == '.' && (rr+1 == r || m[rr+1][b] == '#')) b++;
    b--;
    if (b+1 < c && m[rr][b+1] == '.') ro = 1;
}

int go(int rr, int a, int b, int leftOpen, int rightOpen) {
    if (rr == r-1) return 0;
    //cout << "go " << rr << " " << a << " " << b << " " << leftOpen << " " << rightOpen << endl;
    if (known[rr][a][b][leftOpen][rightOpen]) return dp[rr][a][b][leftOpen][rightOpen];
    known[rr][a][b][leftOpen][rightOpen] = true;

    int best = INF;
    if (leftOpen) {
        int newr = rr, aa, bb, lo, ro; getPlatform(newr, a-1, aa, bb, lo, ro);
        if (aa >= 0) best <?= go(newr, aa, bb, lo, ro);
    }
    if (rightOpen) {
        int newr = rr, aa, bb, lo, ro; getPlatform(newr, b+1, aa, bb, lo, ro);
        if (aa >= 0) best <?= go(newr, aa, bb, lo, ro);
    }

    for (int aa = a; aa <= b; aa++) {
        for (int bb = aa; bb <= b; bb++) {
            for (int i = aa; i <= bb; i++) m[rr+1][i] = '.';

            int digs = bb-aa+1;
            if (aa-1 >= a) {
                int newr = rr, p, q, lo, ro; getPlatform(newr, aa, p, q, lo, ro);
                if (p >= 0) best <?= digs + go(newr, p, q, lo, ro);
            }
            if (bb+1 <= b) {
                int newr = rr, p, q, lo, ro; getPlatform(newr, bb, p, q, lo, ro);
                if (p >= 0) best <?= digs + go(newr, p, q, lo, ro);
            }

            for (int i = aa; i <= bb; i++) m[rr+1][i] = '#';
        }
    }
    //cout << "go " << rr << " " << a << " " << b << " " << leftOpen << " " << rightOpen << " => " << best << endl;
    return dp[rr][a][b][leftOpen][rightOpen] = best;
}

int entryPoint(int caseNo) {
    cin >> r >> c >> f;
    for (int i = 0; i < r; i++) cin >> m[i];
    memset(known, false, sizeof(known));

    int newr = 0, a, b, lo, ro; getPlatform(newr, 0, a, b, lo, ro);
    int best = INF;
    if (a >= 0) best = go(newr, a, b, lo, ro);

    if (best < INF)
        printf("Case #%d: Yes %d\n", caseNo, best);
    else
        printf("Case #%d: No\n", caseNo);
    return 0;
}

int main() {
    int cases; cin >> cases;
    for (int caseNo = 1; caseNo <= cases; caseNo++)
        entryPoint(caseNo);
    return 0;
}
