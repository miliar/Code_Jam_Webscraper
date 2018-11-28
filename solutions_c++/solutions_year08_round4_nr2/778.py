#include <iostream>
#include <algorithm>

using namespace std;

void f(int a, int n, int m){
  int x1 = 0, y1 = 0;
  for (int x2=0; x2<=n; ++x2){
    for (int y2=0; y2<=m; ++y2){
      if (x1 != x2 || y1 != y2){
        for (int x3=0; x3<=n; ++x3){
          for (int y3=0; y3<=m; ++y3){
            if ((x1 != x3 || y1 != y3) && (x2 != x3 || y2 != y3)){
              if ((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) == a){
                printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
                return;
              }
            }
          }
        }
      }
    }
  }
  printf("IMPOSSIBLE\n");
}

int main(){
  int C;
  scanf("%d", &C);
  for (int c=1; c<=C; ++c){
    printf("Case #%d: ", c);
    int a, n, m;
    scanf("%d %d %d", &n, &m, &a);
    if (n*m < a){
      printf("IMPOSSIBLE\n");
    }else{
      f(a, n, m);
    }
  }
  return 0;
}
