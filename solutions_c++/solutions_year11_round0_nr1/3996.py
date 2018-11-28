#include <cstdio>
#include <string.h>
#include <algorithm>
using namespace std;

struct r{
  char rb;
  int loc;
  r(){}
};
r a[110];

int main(){
  int T, ca = 0;
  scanf("%d", &T);
  while (T--){
    int n;
    memset(a, 0, sizeof(a));
    scanf("%d ", &n);
    for (int i=0; i<n; i++){
      scanf("%c %d ", &a[i].rb, &a[i].loc);
    //  printf("%c %d\n", a[i].rb, a[i].loc);
    }
    
    long long s = 0, c[2], t[2], x;
    c[0] = c[1] = 1;
    t[0] = t[1] = 0;
    for (int i=0; i<n; i++){
      if (a[i].rb == 'O') x = 0; else x = 1;
      int d1 = s - t[x];
      int d2 = abs(a[i].loc - c[x]);
      if (d1 > d2){
        s++;
      }else{
        s += d2 - d1 + 1;
      }
      t[x] = s;
      c[x] = a[i].loc;
   //   printf("%d: %d %d %d\n", x, s, t[x], c[x]);
    }
    
    printf("Case #%d: %d\n", ++ca, s);
  }
  return 0;
}
