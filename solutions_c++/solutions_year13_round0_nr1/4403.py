#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;
int test;
string s[10];

bool check(char c) {
    int tt;
    for (int i = 0; i < 4; ++i) {
        tt = 0;
        for (int j = 0 ; j < 4; ++j) 
        if (s[i][j] == c) ++tt;
        if (tt == 4) return true;
    }
    for (int i = 0; i < 4; ++i){
        tt = 0;
        for (int j = 0 ; j < 4; ++j)
            if (s[j][i] == c) ++tt;
        if (tt == 4) return true;
    }
    tt = 0;
    for (int i = 0; i < 4; ++i)
        if (s[i][i] == c) ++tt;
    if (tt == 4) return true;
    tt = 0;
    for (int i = 0 ; i < 4; ++i)
        if (s[i][3 - i] == c) ++tt;
    if (tt == 4) return true;
    return false;
}
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    for (int t = 1; t <= test; ++t) {
        for (int i = 0; i < 4; ++i) cin >> s[i];
        int p = -1;
        for (int i = 0; i < 4; ++i) { 
            for (int j = 0; j < 4; ++j) 
                if (s[i][j] == 'T') {
                    s[i][j] = 'X';
                    if (check('X')) p = 1;
                    s[i][j] = 'O';
                    if (check('O')) p = 0;
                  }
        }
        if (p == -1) if (check('X')) p = 1;
                    else if (check('O')) p = 0;
        cout << "Case #" << t << ": ";
        if (p == -1) {
            for (int i = 0; i < 4; ++i)
                for (int j = 0; j < 4; ++j)
                    if (s[i][j] == '.') p = 1;
            if (p == 1) cout << "Game has not completed" << endl;
            else cout << "Draw" << endl;
        }
        else if (p == 1) cout << "X won" << endl;
        else cout << "O won" << endl; 
    }
    return 0;
}
