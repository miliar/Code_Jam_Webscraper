#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
typedef long long LL;

int solve() {
    char t[4][4];
    for (int i = 0; i < 4; i++) {
        string s;
        cin >> s;
        int x = 0;
        for (int j = 0; j < 4; j++) {
            t[i][j] = s[j];
        }
    }
    bool r1 = true;
    for (int i = 0; i < 4; i++) {
        bool p1 = true;
        bool p2 = true;
        bool p3 = true;
        bool p4 = true;
        bool q1 = true;
        bool q2 = true;
        bool q3 = true;
        bool q4 = true;
        for (int j = 0; j < 4; j++) {
            if (t[i][j] != 'X' && t[i][j] != 'T') p1 = false;
            if (t[j][i] != 'X' && t[j][i] != 'T') p2 = false;
            if (t[i][j] != 'O' && t[i][j] != 'T') q1 = false;
            if (t[j][i] != 'O' && t[j][i] != 'T') q2 = false;
            if (t[i][j] == '.') r1 = false;
            if (t[j][j] != 'X' && t[j][j] != 'T') p3 = false;
            if (t[j][3-j] != 'X' && t[j][3-j] != 'T') p4 = false;
            if (t[j][j] != 'O' && t[j][j] != 'T') q3 = false;
            if (t[j][3-j] != 'O' && t[j][3-j] != 'T') q4 = false;
        }
        if (p1 || p2 || p3 || p4) return 1;
        if (q1 || q2 || q3 || q4) return 2;
    }
    if (r1) return 3;
    return 4;
}

int main() {
    int te;
    scanf("%d", &te);
    for (int i = 1; i <= te; i++) {
        int ret = solve();
        printf("Case #%d: ", i);
        switch(ret) {
            case 1: printf("X won\n"); break;
            case 2: printf("O won\n"); break;
            case 3: printf("Draw\n"); break;
            case 4: printf("Game has not completed\n"); break;
        }
    }
}
