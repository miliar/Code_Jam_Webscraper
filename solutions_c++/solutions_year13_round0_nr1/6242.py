#include <iostream>
#include <cstdio>

using namespace std;

int main(){
  char tablero[4][4];
  int cases,num = 0;
  char in;
  scanf("%i",&cases);
  while(cases--){
    scanf("%c",&in);
    for (int i = 0; i < 4; i++){
      for(int j = 0; j < 4; j++){
        scanf("%c",&in);
        tablero[i][j] = in;
      }
      scanf("%c",&in);
    }

    int xh, yh, xv, yv, xd1= 0, xd2 = 0, yd1=0, yd2=0;
    bool points = false,flag = true;
    for(int i = 0; i < 4; i++){
      xh = yh = xv = yv =  0;
      for(int j = 0; j < 4; j++){
        if(tablero[i][j] == 'T' or tablero[i][j] == 'X') xh++;//,cout<<" h"<<tablero[i][j]<<xh<<"h ";
        if(tablero[i][j] == 'T' or tablero[i][j] == 'O') yh++;
        if(tablero[j][i] == 'T' or tablero[j][i] == 'X') xv++;//,cout<<" v"<<tablero[i][j]<<xh<<"v ";
        if(tablero[j][i] == 'T' or tablero[j][i] == 'O') yv++;
        if(tablero[i][j] == '.' ) points = true;
      }
      if(xh == 4 or xv == 4){
        printf("Case #%i: X won\n", ++num);
        flag = false;
        break;
      }
      if(yh == 4 or yv == 4){
        printf("Case #%i: O won\n", ++num);
        flag = false;
        break;
      }
      if(tablero[i][i] == 'T' or tablero[i][i] == 'X') xd1++;
      if(tablero[i][i] == 'T' or tablero[i][i] == 'O') yd1++;
      if(tablero[i][3-i] == 'T' or tablero[i][3-i] == 'X') xd2++;
      if(tablero[i][3-i] == 'T' or tablero[i][3-i] == 'O') yd2++;
    }
    if((xd1 == 4 or xd2 == 4) and flag) {
      printf("Case #%i: X won\n", ++num);
      continue;
    }
    if((yd1 == 4 or yd2 == 4) and flag) {
      printf("Case #%i: O won\n", ++num);
      continue;
    }
    if(points and flag) {
      printf("Case #%i: Game has not completed\n", ++num);
      continue;
    }
    if(flag) printf("Case #%i: Draw\n", ++num);
  }
  return 0;
}