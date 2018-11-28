#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int cas, CAS, i, j, ans, c[255];
char s[10][10];

int main(){
    freopen("in.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &CAS);
    for (cas = 1; cas <= CAS; cas++){
        for (i = 1; i <= 4; i++) scanf("%s", s[i] + 1);

        ans = 0;
        for (i = 1; i <= 4; i++){
            c['X'] = c['O'] = c['T'] = c['.'] = 0;
            for (j = 1; j <= 4; j++) c[s[i][j]]++;
            if (!c['X'] && c['O'] >= 3 && c['O'] + c['T'] == 4){
                if (ans == 0 || ans == 1) ans = 1; else ans = 3;
            }
            if (!c['0'] && c['X'] >= 3 && c['X'] + c['T'] == 4){
                if (ans == 0 || ans == 2) ans = 2; else ans = 3;
            }
        }
        for (j = 1; j <= 4; j++){
            c['X'] = c['O'] = c['T'] = c['.'] = 0;
            for (i = 1; i <= 4; i++) c[s[i][j]]++;
            if (!c['X'] && c['O'] >= 3 && c['O'] + c['T'] == 4){
                if (ans == 0 || ans == 1) ans = 1; else ans = 3;
            }
            if (!c['0'] && c['X'] >= 3 && c['X'] + c['T'] == 4){
                if (ans == 0 || ans == 2) ans = 2; else ans = 3;
            }
        }
        c['X'] = c['O'] = c['T'] = c['.'] = 0;
        for (i = 1; i <= 4; i++) c[s[i][i]]++;
        if (!c['X'] && c['O'] >= 3 && c['O'] + c['T'] == 4){
            if (ans == 0 || ans == 1) ans = 1; else ans = 3;
        }
        if (!c['0'] && c['X'] >= 3 && c['X'] + c['T'] == 4){
            if (ans == 0 || ans == 2) ans = 2; else ans = 3;
        }
        c['X'] = c['O'] = c['T'] = c['.'] = 0;
        for (i = 1; i <= 4; i++) c[s[i][4 - i + 1]]++;
        if (!c['X'] && c['O'] >= 3 && c['O'] + c['T'] == 4){
            if (ans == 0 || ans == 1) ans = 1; else ans = 3;
        }
        if (!c['0'] && c['X'] >= 3 && c['X'] + c['T'] == 4){
            if (ans == 0 || ans == 2) ans = 2; else ans = 3;
        }
        if (!ans){
            for (i = 1; i <= 4; i++)
            for (j = 1; j <= 4; j++)
            if (s[i][j] == '.') ans = 4;
            if (!ans) ans = 3;
        }
        printf("Case #%d: ", cas);
        if (ans == 1) printf("O won\n");
        if (ans == 2) printf("X won\n");
        if (ans == 3) printf("Draw\n");
        if (ans == 4) printf("Game has not completed\n");
    }


}
