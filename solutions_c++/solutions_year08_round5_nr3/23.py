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

#define PROBLEM "c"

const int INF = 1000000000;

int ans[12][1100];
int seats[12];
int hmuch[1100];

int main(){
  freopen(PROBLEM".in", "r", stdin);
  freopen(PROBLEM".out", "w", stdout);
  int tn, tst;
  scanf("%d", &tn);
  for (tst=1; tst<=tn; tst++){
    printf("Case #%d: ", tst);
    int n, m, i, j, h;
    char ch;
    scanf("%d%d\n", &n, &m);
    for (i=0; i<n; i++){
      seats[i] = 0;
      for (j=0; j<m; j++){
        scanf("%c", &ch);
        if (ch == 'x') seats[i] |= (1 << j);
      }
      scanf("\n");
    }
    for(i=0; i<1024; i++){
      int x=i, s=0;
      while (x > 0){
        s++;
        x &= (x-1);
      }
      hmuch[i] = s;
    }
    memset(ans, 0, sizeof(ans)); 
        int res = -INF;
    for (j=0; j<(1<<m); j++){
      if (((j & (j>>1)) == 0) && ((j & seats[0]) == 0)){
        ans[0][j] = hmuch[j];
      }
      else ans[0][j] = -INF;
      if ((n == 1) && (ans[0][j] > res)) res = ans[0][j];
    }
    for (i=1; i<n; i++){
      for (j=0; j<(1<<m); j++){
        if ((j & seats[i]) || (j & (j>>1))){
          ans[i][j] = -INF;
        }
        else{
          for (h=0; h<(1<<m); h++){
            if ((((h>>1) & j) == 0) && (((h<<1) & j) == 0) && (ans[i-1][h] + hmuch[j] > ans[i][j])){
              ans[i][j] = ans[i-1][h] + hmuch[j];
            }
          } 
        }
        if ((i == n-1) && (ans[i][j] > res)) res = ans[i][j];
      }
    }
    printf("%d\n", res);
  }
  return 0;
}