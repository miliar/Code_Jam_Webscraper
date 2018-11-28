/*
    TASK:
    DATE: 2012-12-09
    STATE: AC
    Solution:
*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#define maxn 1000
#define maxm 100000
#define INF 0x3f3f3f3f
using namespace std;

int n;
string s[5];

bool checkrow(char c) {
    for (int i=1; i<=4; i++) {
        bool f  = true;
        for (int j=0; j<=3; j++) f &= (s[i][j] == c || s[i][j] == 'T');
        if (f) return true;
    }
    return false;
}

bool checkcol(char c) {
    for (int i=0; i<4; i++) {
        bool f  = true;
        for (int j=1; j<=4; j++) f &= (s[j][i] == c || s[j][i] == 'T');
        if (f) return true;
    }
    return false;
}

bool checkxie(char c) {
    bool f = true;
    for (int i=0; i<4; i++)
        f &= (s[i + 1][i] == c || s[i + 1][i] == 'T');
    if (f) return f;
    
    f = true;
    for (int i=1; i<=4; i++)
        f &= (s[i][4 - i] == c || s[i][4 - i] == 'T');
    return f;
}

int check() {
    //check row
    if (checkrow('X')) return 1;
    if (checkrow('O')) return 2;
    //check col
    if (checkcol('X')) return 1;
    if (checkcol('O')) return 2;

    //check xie
    if (checkxie('X')) return 1;
    if (checkxie('O')) return 2;

    //check draw
    bool flag = true;
    for (int i=1; i<=4; i++)
        for (int j=0; j<4; j++) flag &= s[i][j] != '.';

    if (flag) return 0; else return 3;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d\n", &n);
    for(int t=1; t<=n; t++) {
        for (int i=1; i<=4; i++) cin >> s[i];
//        for (int i=1; i<=4; i++) cout << s[i] << endl;
//        cout << endl;
        int ans = check();
        printf("Case #%d: ", t);
        if (ans == 0) puts("Draw");
        if (ans == 1) puts("X won");
        if (ans == 2) puts("O won");
        if (ans == 3) puts("Game has not completed");
    }
    return 0;
    fclose(stdout);
}
