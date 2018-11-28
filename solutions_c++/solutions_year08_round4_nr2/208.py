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


int main(){
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int tn, tst;
  scanf("%d", &tn);
  for (tst=1; tst<=tn; tst++){
    printf("Case #%d: ", tst);
    int n, m, a;
    scanf("%d%d%d", &n, &m, &a);
    int i, j, k, h, f = 0;
    for (i=0; i<=n; i++){
      for (j=0; j<=m; j++){
        for (k=0; k<=n; k++){
          for (h=0; h<=m; h++){
            int s = (k-i)*j + i*h;
            if (s < 0) s = -s;
            if (s == a){
              f = 1;
              goto zzz;
            }
          }
        }
      }
    }zzz:;
    if (!f) printf("IMPOSSIBLE");
    else printf("%d %d %d %d %d %d", i, 0, 0, j, k, h);
    printf("\n");
  }
  return 0;
}