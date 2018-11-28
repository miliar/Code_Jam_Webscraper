// Problem A. Tic-Tac-Toe-Tomek
// Contest: Google CodeJam Qualification Round 2013
// Author: LotK

#include <cstdio>

int main() {
  int t, tt, i, j, ans;
  char a[4][5];
  scanf("%d", &tt);
  for(t=0 ; t<tt ; t++) {
    for(i=0 ; i<4 ; i++) {
      scanf("%s", a[i]);
    }

    ans=0;

    // X won -----------------------------------------
    for(i=0 ; i<4 ; i++) {
      for(j=0 ; j<4 ; j++) {
        if(a[i][j]!='X' && a[i][j]!='T') break;
      }
      if(j==4) ans=1;
      for(j=0 ; j<4 ; j++) {
        if(a[j][i]!='X' && a[j][i]!='T') break;
      }
      if(j==4) ans=1;
    }
    // diagonal
    for(i=0 ; i<4 ; i++) {
        if(a[i][i]!='X' && a[i][i]!='T') break;
    }
    if(i==4) ans=1;
    for(i=0 ; i<4 ; i++) {
        if(a[i][3-i]!='X' && a[i][3-i]!='T') break;
    }
    if(i==4) ans=1;


    // O won -------------------------------------------
    for(i=0 ; i<4 ; i++) {
      for(j=0 ; j<4 ; j++) {
        if(a[i][j]!='O' && a[i][j]!='T') break;
      }
      if(j==4) ans=2;
      for(j=0 ; j<4 ; j++) {
        if(a[j][i]!='O' && a[j][i]!='T') break;
      }
      if(j==4) ans=2;
    }
    // diagonal
    for(i=0 ; i<4 ; i++) {
        if(a[i][i]!='O' && a[i][i]!='T') break;
    }
    if(i==4) ans=2;
    for(i=0 ; i<4 ; i++) {
        if(a[i][3-i]!='O' && a[i][3-i]!='T') break;
    }
    if(i==4) ans=2;


    // draw -------------------------------------
    for(i=0 ; i<4 ; i++) {
      for(j=0 ; j<4 ; j++) {
        if(a[i][j]=='.') break;
      }
      if(j<4) break;
    }
    if(i==4 && ans==0) ans = 3;


    printf("Case #%d: ", t+1);
    if(ans==1) printf("X won\n");
    else if(ans==2) printf("O won\n");
    else if(ans==3) printf("Draw\n");
    else printf("Game has not completed\n");
  }
}
