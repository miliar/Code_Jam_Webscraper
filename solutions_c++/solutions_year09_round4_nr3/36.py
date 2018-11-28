#include <cstdio>
#include <set>
#include <string>
#include <cstring>

using namespace std;

const int MAX = 256;

int n, k, ans, ok;
int chart[MAX][MAX];
char used[MAX], paint[MAX];
int con[MAX][MAX];

void dfs(int a){
  if (a>=n && !paint[a]){
    paint[a] = 1;
    ok = 1;
    return;
  }
  used[a] = 1;
  int i;
  for (i=0; i<2*n; i++){
    if (con[a][i] && !used[i]){
      dfs(i);
      if (ok){
        con[a][i] = 0;
        con[i][a] = 1;
        return;
      }
    }
  }
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    scanf("%d%d", &n, &k);
    int i, j, h;
    for (i=0; i<n; i++){
      for (j=0; j<k; j++){
        scanf("%d", &chart[i][j]);
      }
    }
    memset(con, 0, sizeof(con));
    for (i=0; i<n; i++){
      for (j=0; j<n; j++){
        int ok = 1;
        for (h=0; h<k; h++){
          if (chart[i][h] >= chart[j][h]){
            ok = 0;
            break;
          }
        }
        con[i][j+n]=ok;
      }
    }
    ans = 0;
    memset(paint, 0, sizeof(paint));
    for (i=0; i<n; i++){
      memset(used, 0, sizeof(used));
      ok = 0;
      dfs(i);
      ans += ok;
    }
    printf("%d\n", n - ans);
  }
  return 0;
}
