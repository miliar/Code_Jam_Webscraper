#include <iomanip>
#include <stdio.h>
#include <map>
#include <set>

using namespace std;
int main(){
  FILE *in = fopen("A-small-0.in","r");
  FILE *out = fopen("small.out","w");
  int T;
  fscanf(in,"%d ", &T);
  for (int t = 0; t < T; t++){
    char table[110][110]={};
    int R,C; char tmpc;
    fscanf(in,"%d %d ", &R, &C);
    for (int i = 0; i < R; i++){
      for (int j = 0; j< C; j++){
        fscanf(in," %c ",&table[i][j]);
      }
    }
    bool changed=true, posible=true;
    while (changed && posible){
      changed=false;
    for (int i = 0; i < R; i++){
      for (int j = 0; j< C; j++){
          if(table[i][j] =='#'){
            changed=true;
            if (table[i][j+1]=='#' && table[i+1][j]=='#' && table[i+1][j+1]=='#'){
              table[i][j]='/'; table[i][j+1]='\\'; table[i+1][j]='\\'; table[i+1][j+1]='/';
            }else posible=false;
          }
        }
      }
    }
    
    printf("Case #%d:\n",t+1);
    if (posible){
      for (int i = 0; i < R; i++){
        for (int j = 0; j< C; j++){
          printf("%c",table[i][j]);
        }
        printf("\n");
    }
    }else
      printf("Impossible\n");

  }
    
}
