#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
bool checkX(char a,char b, char c, char d) {
  return a == 'X' && b == 'X' && c == 'X' && d == 'X';
}
bool checkO(char a,char b, char c, char d) {
  return a == 'O' && b == 'O' && c == 'O' && d == 'O';
}
int main() {
  int t;
  FILE* fout = fopen("output.txt","w");
  FILE* fin = fopen("input.txt","r");
  fscanf(fin, "%d", &t);
  for(int k = 1; k <= t; k ++) {
    char map[4][4], mapO[4][4], mapX[4][4];
    int ck = 0, full = 0;
    for(int i = 0; i < 4; i ++)
      for(int j = 0; j < 4; j ++) {
        fscanf(fin, "%c", &map[i][j]);
        if(map[i][j] == '\n')
          j --;
      }
    for(int i = 0; i < 4; i ++)
      for(int j = 0; j < 4; j ++) {
        if(map[i][j] == 'T') {
          mapO[i][j] = 'O';
          mapX[i][j] = 'X';
        }
        else{
          if(map[i][j] == '.')
            full ++;
          mapO[i][j] = map[i][j];
          mapX[i][j] = map[i][j];
        }
      }
    fprintf(fout, "Case #%d: ", k);
    for(int i = 0; i < 4; i ++)
      if(checkX(mapX[i][0], mapX[i][1], mapX[i][2], mapX[i][3]) == true) {
        fprintf(fout, "X won\n");
        ck = 1;
        break;
      }
    if(ck == 1)
      continue;
    for(int i = 0; i < 4; i ++)
      if(checkX(mapX[0][i], mapX[1][i], mapX[2][i], mapX[3][i]) == true) {
        fprintf(fout, "X won\n");
        ck = 1;
        break;
      }
    if(ck == 1)
      continue;
    if(checkX(mapX[0][0], mapX[1][1], mapX[2][2], mapX[3][3]) == true) {
        fprintf(fout, "X won\n");
        continue;
      }
    if(checkX(mapX[0][3], mapX[1][2], mapX[2][1], mapX[3][0]) == true) {
        fprintf(fout, "X won\n");
        continue;
      }
    for(int i = 0; i < 4; i ++)
      if(checkO(mapO[i][0], mapO[i][1], mapO[i][2], mapO[i][3]) == true) {
        fprintf(fout, "O won\n");
        ck = 1;
        break;
      }
    if(ck == 1)
      continue;
    for(int i = 0; i < 4; i ++)
      if(checkO(mapO[0][i], mapO[1][i], mapO[2][i], mapO[3][i]) == true) {
        fprintf(fout, "O won\n");
        ck = 1;
        break;
      }
    if(ck == 1)
      continue;
    if(checkO(mapO[0][0], mapO[1][1], mapO[2][2], mapO[3][3]) == true) {
        fprintf(fout, "O won\n");
        continue;
      }
    if(checkO(mapO[0][3], mapO[1][2], mapO[2][1], mapO[3][0]) == true) {
        fprintf(fout, "O won\n");
        continue;
      }
    if(full == 0)
      fprintf(fout, "Draw\n");
    else
      fprintf(fout, "Game has not completed\n");
  }
  return 0;
}
