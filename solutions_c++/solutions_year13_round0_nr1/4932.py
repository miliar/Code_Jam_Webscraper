#include <iostream>
#include <cstdio>
#include <cstring>
#define rep(i,l,r) for (int i = l;i <= r;i ++)
#define drep(i,r,l) for (int i = r;i >= l;i --)
using namespace std;

char map[4][4];

bool check (char c){
    int i,j;
    for (i = 0;i <= 3;i ++){
        for (j = 0;j <= 3;j ++){
            if (map[i][j] != c && map[i][j] != 'T') break;
        }
        if (j > 3) return true;
        for (j = 0;j <= 3;j ++){
            if (map[j][i] != c && map[j][i] != 'T') break;
        }
        if (j > 3) return true;
    }
    for (i = 0;i <= 3;i ++){
        if (map[i][i] != c && map[i][i] != 'T') break;
    }
    if (i > 3) return true;
    for (i = 0;i <= 3;i ++){
        if (map[i][3 - i] != c && map[i][3 - i] != 'T') break;
    }
    if (i > 3) return true;
    return false;
}

int main (){
    int cas,c = 0,ans;
    scanf ("%d",&cas);
    while (cas --){
        ans = 0;
        rep (i,0,3) {
            scanf ("%s",map[i]);
            rep (j,0,3) {
                if (map[i][j] == '.') ans ++;
            }
        }
        printf ("Case #%d: ",++ c);
        if (check('X')) puts("X won");
        else if (check('O')) puts ("O won");
        else if (ans == 0) puts ("Draw");
        else puts ("Game has not completed");
    }
    return 0;
}