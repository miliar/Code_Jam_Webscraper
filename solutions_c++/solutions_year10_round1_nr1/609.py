#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

const int mov[4][2] = {0,1, 1,0, 1,1, 1,-1};

char Str[60][60], Board[60][60];
int n, m;


void input(){
    int i;
    scanf("%d%d", &n, &m);
    for (i = 0; i < n; ++ i){
        scanf("%s", Str[i]);
    }
}

void printBoard(char M[][60]){
    int i;
    for (i = 0; i < n; ++ i){
        printf("%s\n", M[i]);
    }
    putchar(10);
}

void rotate(){
    int i, j;
    for (i = 0; i < n; ++ i){
        for (j = 0; j < n; ++ j){
            Board[j][n - i - 1] = Str[i][j];
        }
    }
    //printBoard(Board);
    int ti;
    for (j = 0; j < n; ++ j){
        ti = n - 1;
        for (i = n - 1; i >= 0; -- i){
            if (Board[i][j] != '.'){
                Board[ti][j] = Board[i][j];
                -- ti;
            }
        }
        for (;ti >= 0; -- ti){
            Board[ti][j] = '.';
        }
    }
    //printBoard(Board);
}

inline bool pass(int x, int y, char t){
    if (x < 0 || x >= n) return false;
    if (y < 0 || y >= n) return false;
    if (Board[x][y] != t) return false;
    return true;
}

int check(int x, int y){
    int lx, ly, rx, ry, i;
    char type = Board[x][y];
    for (i = 0; i < 4; ++ i){
        lx = rx = x;
        ly = ry = y;
        do{
            lx -= mov[i][0];
            ly -= mov[i][1];
        }while (pass(lx, ly, type));
        lx += mov[i][0];
        ly += mov[i][1];
        do{
            rx += mov[i][0];
            ry += mov[i][1];
        }while (pass(rx, ry, type));
        rx -= mov[i][0];
        ry -= mov[i][1];
        //printf("%d %d %d %d\n", x, y, lx, rx);
        if (abs(rx - lx) + 1 >= m){
            return type == 'R'? 1 : 2;
        }
        if (abs(ry - ly) + 1 >= m){
            return type == 'R'? 1 : 2;
        }
    }
    return 0;
}

void solve(){
    rotate();
    int i, j, ans = 0;
    //printBoard(Board);
    for (i = 0; i < n; ++ i){
        for (j = 0; j < n; ++ j){
            if (Board[i][j] == '.') continue;
            if ((Board[i][j] == 'R') && (!(ans & 1))){
                ans |= check(i, j);
            }
            if ((Board[i][j] == 'B') && (!(ans & 2))){
                ans |= check(i, j);
            }
        }
    }
    switch (ans){
        case 3:
            puts("Both"); break;
        case 2:
            puts("Blue"); break;
        case 1:
            puts("Red"); break;
        case 0:
            puts("Neither"); break;
    }
}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, ti = 0;
    scanf("%d", &t);
    while (t --){
        input();
        printf("Case #%d: ", ++ ti);
        solve();
    }
    return 0;
}
    
