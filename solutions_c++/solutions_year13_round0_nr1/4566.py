#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

FILE *in = fopen("A.in", "r");
FILE *out = fopen("A.out", "w");

char g[55][55];
int move[4][2] = {{0, 1}, {1, 0}, {1, 1}, {-1, 1}};

void count3(int x, int y, int d, int &O, int &X, int &T){
  while(x >= 0 && x < 4 && y >= 0 && y < 4){
    if(g[x][y] == 'O') O ++;
    if(g[x][y] == 'X') X ++;
    if(g[x][y] == 'T') T ++;
    x += move[d][0];
    y += move[d][1];
  }
}

int main(){
  int TEST;
  fscanf(in, "%d\n", &TEST);
  for(int test = 1; test <= TEST; test++){
    for(int q = 0; q < 4; q++){
      fscanf(in, "%s", g[q]);
    }
    
    for(int q = 0; q < 4; q++){
      for(int w = 0; w < 4; w++){
        for(int d = 0; d < 4; d++){
          int O = 0, X = 0, T = 0;
          count3(q, w, d, O, X, T);
          if(O + T == 4){
            fprintf(out, "Case #%d: O won\n", test);
            goto FINISH;
          }
          if(X + T == 4){
            fprintf(out, "Case #%d: X won\n", test);
            goto FINISH;
          }
        }
      }
    }
    
    for(int q = 0; q < 4; q++){
      for(int w = 0; w < 4; w++){
        if(g[q][w] == '.'){
          fprintf(out, "Case #%d: Game has not completed\n", test);
          goto FINISH;
        }
      }
    }
    fprintf(out, "Case #%d: Draw\n", test);
    FINISH:;
  }
  return 0;
}
