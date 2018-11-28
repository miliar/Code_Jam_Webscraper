#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

const int n = 4;

int map[n][n];

int getch() {
    int ch = 0;
    while (ch = getchar())
          if (ch == '.' || ch == 'O' || ch == 'X' || ch == 'T') break;
    return ch;
}

void init() {
     for (int i = 0; i < 4; i++ )
         for (int j = 0; j < 4; j++ )
             map[i][j] = getch();
}

bool checkwin(int ch ) {
     int cnt;
     for (int i = 0; i < 4; i++ ) {
         cnt = 0;
         for (int j = 0; j < 4; j++ )
             if (map[i][j] == ch || map[i][j] == 'T') ++cnt;
         if (cnt == 4) return true;
     }
     for (int j = 0; j < 4; j++ ) {
         cnt = 0;
         for (int i = 0; i < 4; i++ )
             if (map[i][j] == ch || map[i][j] == 'T') ++cnt;
         if (cnt == 4) return true;
     }
     cnt = 0;
     for (int i = 0; i < 4; i++ )
         if (map[i][i] == ch || map[i][i] == 'T') ++cnt;
     if (cnt == 4) return true;
     cnt = 0;
     for (int i = 0; i < 4; i++ )
         if (map[i][3-i] == ch || map[i][3-i] == 'T') ++cnt;
     if (cnt == 4) return true;
     return false;
}

void work() {
     bool draw = true;
     for (int i = 0; i < 4; i++ )
         for (int j = 0; j < 4; j++ )
             if (map[i][j] == '.') draw = false;
     if (checkwin('X'))
        printf("X won\n");
     else if (checkwin('O'))
        printf("O won\n");
     else if (draw)
          printf("Draw\n");
     else
         printf("Game has not completed\n");
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cas;
    scanf("%d",&cas);
    for (int run = 1; run <= cas; run++ ) {
        printf("Case #%d: ", run);
        init();
        work();
    }
    return 0;
}
