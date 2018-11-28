#include <stdio.h>

char str[10][10];

bool isnotc() {
     for (int i = 0; i < 4; ++i) {
         for (int j = 0; str[i][j] != 0; ++j) {
             if (str[i][j] == '.') {
                return true;
             }
         }
     }
     return false;
}

int dir[][2] = {{1,0},{0,1},{-1,0},{0,-1},{1,1},{-1,-1},{1,-1},{-1,1}};

bool has4(int x,int y) {
     for (int i = 0; i < 8; ++i) {
         int j;
         for (j = 0; j < 4; ++j) {
             int tmpx = x+dir[i][0]*j;
             int tmpy = y+dir[i][1]*j;
             if (tmpx < 0 || tmpx >= 4) break;
             if (tmpy < 0 || tmpy >= 4) break;
             if (str[tmpx][tmpy] != 'T' && str[tmpx][tmpy] != str[x][y]) {
                break;
             }
         }
         if (j == 4) return true; 
     }
     return false;
}

bool win(char c) {
     for (int i = 0; i < 4; ++i) {
         for (int j = 0; j < 4; ++j) {
             if (str[i][j] == c && has4(i,j) ) {
                return true;
             }     
         }
     }
     return false;
}

int main () {
    int kase, h = 1;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          for (int i = 0; i < 4; ++i) {
              scanf("%s", str[i]);
          }
          printf("Case #%d: ",h++);
          if ( win('X') == 1 ) {
             printf("X won\n");
          }
          else if ( win('O') == 1 ) {
               printf("O won\n");
          }
          else if ( isnotc() ) {
             printf("Game has not completed\n");
          }
          else {
               printf("Draw\n");
          }
    }
    return 0;
}
