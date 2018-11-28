#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

bool bit(int64 mask, int k) {
    return ((1LL << k) & mask) != 0;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        cerr << "Case #" << testNumber << "..." << endl;
        int n = 4;
        vector<string> table(n);
        for (int i = 0; i < n; ++i) {
            cin >> table[i];
        }
        bool xwon = false;
        bool owon = false;
        bool hasempty = false;
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            ok = true;
            for (int j = 0; j < n; ++j) {
                char c = table[i][j];
                if (c != 'X' && c != 'T')
                    ok = false;
            }
            if (ok) xwon = true;

            ok = true;
            for (int j = 0; j < n; ++j) {
                char c = table[j][i];
                if (c != 'X' && c != 'T')
                    ok = false;
            }
            if (ok) xwon = true;

            ok = true;
            for (int j = 0; j < n; ++j) {
                char c = table[i][j];
                if (c != 'O' && c != 'T')
                    ok = false;
            }
            if (ok) owon = true;

            ok = true;
            for (int j = 0; j < n; ++j) {
                char c = table[j][i];
                if (c != 'O' && c != 'T')
                    ok = false;
            }
            if (ok) owon = true;
        }
        ok = true;
        for (int j = 0; j < n; ++j) {
            char c = table[j][j];
            if (c != 'X' && c != 'T')
                ok = false;
        }
        if (ok) xwon = true;

        ok = true;
        for (int j = 0; j < n; ++j) {
            char c = table[j][n - 1 - j];
            if (c != 'X' && c != 'T')
                ok = false;
        }
        if (ok) xwon = true;

        ok = true;
        for (int j = 0; j < n; ++j) {
            char c = table[j][j];
            if (c != 'O' && c != 'T')
                ok = false;
        }
        if (ok) owon = true;

        ok = true;
        for (int j = 0; j < n; ++j) {
            char c = table[j][n - 1 - j];
            if (c != 'O' && c != 'T')
                ok = false;
        }
        if (ok) owon = true;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (table[i][j] == '.') hasempty = true;
            }
        }

        string res = "Draw";
        assert(!xwon || !owon);
        if (xwon) res = "X won";
        else if (owon) res = "O won";
        else if (hasempty) res = "Game has not completed";

        cout << "Case #" << testNumber << ": " << res << endl;
    }

    return 0;
}