#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

bool won(vector<string> a, char ch) {
    int res = 0;
    for (int i = 0; i < 4; ++i) {
        int cnt = 0;
        for (int j = 0; j < 4; ++j)
            if (a[i][j] == ch || a[i][j] == 'T')
                ++cnt;
        res = max(res, cnt);
    }
    for (int j = 0; j < 4; ++j) {
        int cnt = 0;
        for (int i = 0; i < 4; ++i)
            if (a[i][j] == ch || a[i][j] == 'T')
                ++cnt;
        res = max(res, cnt);
    }
    int cnt = 0;
    for (int i = 0; i < 4; ++i)
        if (a[i][i] == ch || a[i][i] == 'T')
            ++cnt;
    res = max(res, cnt);
    cnt = 0;
    for (int i = 0; i < 4; ++i)
        if (a[i][3 - i] == ch || a[i][3 - i] == 'T')
           ++cnt;
    res = max(res, cnt);
    return res == 4;
}

void solve() {
    vector<string> a(4);
    for (int i = 0; i < 4; ++i)
        cin >> a[i];
    if (won(a, 'X')) {
        cout << "X won" << endl;
        return;
    }
    if (won(a, 'O')) {
        cout << "O won" << endl;
        return;
    }
    int cnt = 0;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (a[i][j] != '.')
                ++cnt;
    if (cnt == 16)
        cout << "Draw" << endl;
    else
        cout << "Game has not completed" << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
