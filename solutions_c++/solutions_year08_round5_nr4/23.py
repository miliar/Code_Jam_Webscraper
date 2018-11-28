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

#define PROBLEM "d"

const int MOD = 10007;

int field[110][110];
int ans[110][110];

int main(){
  freopen(PROBLEM".in", "r", stdin);
  freopen(PROBLEM".out", "w", stdout);
  int tn, tst;
  scanf("%d", &tn);
  for (tst=1; tst<=tn; tst++){
    printf("Case #%d: ", tst);
    int n, m, r, a, b, i, j;
    scanf("%d%d%d", &n, &m, &r);
    memset(field, 0, sizeof(field));
    memset(ans, 0, sizeof(ans));
    for (i=1; i<=r; i++){
      scanf("%d%d", &a, &b);
      field[a][b] = 1;
    }
    ans[1][1] = 1;
    for (i=2; i<=n; i++){
      for (j=1; j<=m; j++){
        if (!field[i][j]){
          if ((i>=3) && (j>=2)) ans[i][j] += ans[i-2][j-1];
          if (j>=3) ans[i][j] += ans[i-1][j-2];
          ans[i][j] %= MOD;
        }
      } 
    }
    printf("%d\n", ans[n][m]);
  }
  return 0;
}