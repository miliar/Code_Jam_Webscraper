#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>

int n, m;
char gmatr[2010][2010];
int gpow[2010];
int cmilk[2010];
char used[2010];

int main(){
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    printf("Case #%d:", t);
    scanf("%d%d", &n, &m);
    int i, z, j, x, y;
    memset(cmilk, 0, sizeof(cmilk));
    memset(gmatr, 0, sizeof(gmatr));
    memset(gpow, 0, sizeof(gpow));
    memset(used, 0, sizeof(used));
    for (i=1; i<=m; i++){
      scanf("%d", &z);
      for (j=0; j<z; j++){
        scanf("%d%d", &x, &y);
        if (y == 1) cmilk[i] = x;
        else{
          gmatr[i][x] = 1;
          gpow[i]++;
        }
      }
    }
    int ok = 1;
    for (i=1; i<=n; i++){
      int totake = 0;
      for (j=1; j<=m; j++){
        if ((gpow[j])||(used[cmilk[j]])) continue;
        if (cmilk[j] == 0) ok = 0;
        else totake = cmilk[j];
      }
      if ((!ok)||(!totake)) break;
      used[totake] = 1;
      for (j=1; j<=m; j++){
        if (gmatr[j][totake]){
          gmatr[j][totake] = 0;
          gpow[j]--;
        }
      }
    }
    for (j=1; j<=m; j++){
      if ((gpow[j] == 0) && (cmilk[j] == 0)) ok = 0;
    }
    if (!ok) printf(" IMPOSSIBLE\n");
    else{
      for (i=1; i<=n; i++) printf(" %d", used[i]);
      printf("\n");
    }
  }
  return 0;
}