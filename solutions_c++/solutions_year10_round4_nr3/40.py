#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int total;
char field[128][128];

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn;
  scanf("%d", &tn);
  for (int t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    memset(field, 0, sizeof(field));
    int r, lx, ly, rx, ry;
    scanf("%d", &r);
    for (int i=0; i<r; i++){
      scanf("%d%d%d%d", &lx, &ly, &rx, &ry);
      for (int x=lx; x<=rx; x++){
        for (int y=ly; y<=ry; y++){
          if (!field[x][y]) total++;
          field[x][y] = 1;          
        }
      }
    }
    int moves = 0;
    while (total > 0){
      moves++;
      for (int x=100; x>=1; x--){
        for (int y=100; y>=1; y--){
          if (!field[x][y] && field[x-1][y] && field[x][y-1]){
            field[x][y] = 1;
            total++;
          }
          if (field[x][y] && !field[x-1][y] && !field[x][y-1]){
            field[x][y] = 0;
            total--;
          }
        }
      }
    }
    printf("%d\n", moves);
    fflush(stdout);
  }
  return 0;
}
