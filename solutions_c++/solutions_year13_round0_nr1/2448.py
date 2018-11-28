#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int N = 5;

int mp1[N][N], mp2[N][N];
int tm[256];

int check(int mp[N][N]) {
    int calc[3][N];
    memset(calc, 0, sizeof(calc));

    calc[2][0] = calc[2][1] = 3;
    for (int i = 0; i < 4; i++) {
        calc[0][i] = calc[1][i] = 3;
        for (int j = 0; j < 4; j++) {
            calc[0][i] &= mp[i][j];
            calc[1][i] &= mp[j][i];
        }
        calc[2][0] &= mp[i][i];
        calc[2][1] &= mp[i][3 - i];
    }

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            if (calc[i][j]) return calc[i][j];
        }
    }
    return 0;
}

int main() {
    freopen("d://in.txt", "r", stdin);
    freopen("d://out.txt", "w", stdout);

    char buf[N];
    tm['X'] = 1;
    tm['O'] = 2;
    tm['T'] = 3;
    tm['.'] = 0;

    int t;
    scanf("%d", &t);gets(buf);
    for (int ti = 1; ti <= t; ti++) {
        memset(mp1, 0, sizeof(mp1));
        memset(mp2, 0, sizeof(mp2));
        for (int i = 0; i < 4; i++) {
            gets(buf);
            for (int j = 0; j < 4; j++) {
                mp2[i][j] = mp1[i][j] = tm[buf[j]];
                if (mp2[i][j] == 0) mp2[i][j] = 3;
            }
        }
        gets(buf);
        int v1 = check(mp1);
        int v2 = check(mp2);
        printf("Case #%d: ", ti);
        if (v1)
            printf("%c won", v1 == 1 ? 'X' : 'O');
        else if (v2)
            printf("Game has not completed");
        else
            printf("Draw");
        printf("\n");
    }
    //system("pause");
    return 0;
}