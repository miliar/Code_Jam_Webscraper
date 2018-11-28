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

int n, k;
char field[55][55];
int dirs[4][2]={{1,0},{0,1},{-1,1},{1,1}};

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn;
  scanf("%d", &tn);
  for (int t=1; t<=tn; t++){
    scanf("%d%d\n", &n, &k);
    for (int i=0; i<n; i++){
      for (int j=0; j<n; j++){
        scanf("%c", &field[j][n-1-i]);
      }
      scanf("\n");
    }
    for (int j=0; j<n; j++){
      int hei=n-1;
      for (int i=n-1; i>=0; i--){
        if (field[i][j] != '.'){
          field[hei][j] = field[i][j];
          if (hei > i) field[i][j] = '.';
          hei--;
        }
      }
    }
    bool isr=false, isb=false;
    for (int i=0; i<n; i++){
      for (int j=0; j<n; j++){
        if (field[i][j] == '.') continue;
        for (int dir=0; dir<4; dir++){
          bool ok = true;
          for (int s=0; s<k; s++){
            int ni = i + s * dirs[dir][0];
            int nj = j + s * dirs[dir][1];
            ok &= (ni>=0 && ni<n && nj>=0 && nj<n && field[i][j]==field[ni][nj]);
          }
          if (ok){
            if (field[i][j]=='R') isr = true;
            else isb = true;
          }
        }
      }
    }
    printf("Case #%d: ", t);
    if (isr && isb) printf("Both");
    else if (isr) printf("Red");
    else if (isb) printf("Blue");
    else printf("Neither");
    printf("\n");
  }
  return 0;
}
