#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdlib>
using namespace std;

int m;
int types[10100];
int is_ch[10100];
int ans[10100][2];

int main(){
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int tn, tst;
  scanf("%d", &tn);
  for (tst=1; tst<=tn; tst++){
    printf("Case #%d: ", tst);
    int i, x, v;
    scanf("%d%d", &m, &v);
    memset(ans, 0x3f, sizeof(ans));
    for (i=1; i<=(m-1)/2; i++){
      scanf("%d%d", &types[i], &is_ch[i]);
    }
    for (i=(m-1)/2+1; i<=m; i++){
      scanf("%d", &x);
      ans[i][x] = 0;
    }
    for (i=(m-1)/2; i>=1; i--){
      int j, h, ch;
      for (j=0; j<=1; j++){
        for (h=0; h<=1; h++){
          for (ch=0; ch<=1; ch++){
            if (ch && !is_ch[i]) continue;
            int cres = ans[2*i][j] + ans[2*i+1][h] + ch;
            int val;
            if ((types[i] + ch) & 1){
              val = j & h;
            }
            else{
              val = j | h;
            }
            if (ans[i][val] > cres) ans[i][val] = cres;
          }
        }
      }
    }
    if (ans[1][v] < 0x3f3f3f3f){
      printf("%d\n", ans[1][v]);
    }
    else printf("IMPOSSIBLE\n");
  }
  return 0;
}