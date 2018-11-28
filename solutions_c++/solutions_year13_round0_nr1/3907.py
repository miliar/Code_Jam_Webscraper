#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#include <sstream>
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
using namespace std;

typedef long long ll;

string s[4];

bool check(char c) {
    int i, j;
    bool ok;
    fo(i,4) {
        ok = true;
        fo(j,4) {
            if (s[i][j] != c && s[i][j] != 'T')
                ok = false;
        }
        if (ok) return true;
    }

    fo(i,4) {
        ok = true;
        fo(j,4) {
            if (s[j][i] != c && s[j][i] != 'T')
                ok = false;
        }
        if (ok) return true;
    }

    ok = true;
    fo(i,4) if (s[i][i] != c && s[i][i] != 'T') ok = false;
    if (ok) return true;
    ok = true;
    fo(i,4) if (s[i][3-i] != c && s[i][3-i] != 'T') ok = false;
    return ok;
}

int main(void) {
    int t, tt;
    cin >> t;
    fo(tt, t) {
        int i, j;
        fo(i,4) {
            cin >> s[i];
        }

        cout << "Case #" << tt + 1 << ": ";
        if (check('X')) {
            cout << "X won" << endl;
            continue;
        }
        if (check('O')) {
            cout << "O won" << endl;
            continue;
        }
        bool over = true;
        fo(i,4) fo(j,4) if (s[i][j] == '.') over = false;
        if (!over) {
            cout << "Game has not completed" << endl;
            continue;
        }
        cout << "Draw" << endl;
    }
}
