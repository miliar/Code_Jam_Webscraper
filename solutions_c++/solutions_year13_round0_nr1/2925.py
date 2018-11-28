#include <iostream>
#include <cstdio>
#include <memory.h>
using namespace std;
char map[5][5];

void read() {
    for (int i=0;i<4;i++) {
        getchar();
        scanf("%s",map[i]);
    }
    return;
}

bool full() {
    for (int i=0;i<4;i++) {
        for (int j=0;j<4;j++) {
            if(map[i][j] == '.') return false;
        }
    }
    return true;
}

bool check(char c) {
    for (int i=0;i<4;i++) {
        if (map[i][0] == c && map[i][1] == c &&
            map[i][2] == c && map[i][3] == c) return true;
        if (map[0][i] == c && map[1][i] == c &&
            map[2][i] == c && map[3][i] == c) return true;
    }
    return false;
}

bool  diagonal(char c) {
    if (map[0][0] == c && map[1][1] == c &&
        map[2][2] == c && map[3][3] == c) return true;
    if (map[0][3] == c && map[1][2] == c &&
        map[2][1] == c && map[3][0] == c) return true;
    return false;
}

void solve() {
    int x = -1,y = -1;
    for (int i=0;i<4;i++) {
        for (int j=0;j<4;j++) {
            if(map[i][j] == 'T') {
                x = i;
                y = j;
                break;
            }
        }
        if (x != -1) break;
    }
    if (x != -1) map[x][y] = 'X';
    if (check('X') || diagonal('X')) {
        puts("X won");
        return;
    }
    if (x != -1) map[x][y] = 'O';
    if (check('O') || diagonal('O')) {
        puts("O won");
        return;
    }
    if (full()) puts("Draw");
    else puts("Game has not completed");
    return;
}

int main() {
    //freopen("in.txt","r",stdin);
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int i=1;i<=cas;i++) {
        printf("Case #%d: ",i);
        read();
        solve();
    }
    return 0;
}
