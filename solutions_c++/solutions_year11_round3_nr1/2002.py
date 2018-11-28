#include <cstdio>
#include <string.h>

char s[10];
char a[60][60];
int n, m;

bool chk(int x, int y){
  if (0 <= x && x < n && 0 <= y && y < m && a[x][y] == '#')
    return true;
  return false;
}

bool fill(int x, int y){
  if (chk(x, y) && chk(x, y+1) && chk(x+1, y) && chk(x+1, y+1)){
    a[x][y] = '/';
    a[x][y+1] = '\\';
    a[x+1][y] = '\\';
    a[x+1][y+1] = '/';
  }
}

int main(){
  int T, ca=0;
  scanf("%d", &T);
  while (T--){

    scanf("%d%d", &n, &m);
    gets(s);
    memset(a, 0, sizeof(a));
    for (int i=0; i<n; i++)
      gets(a[i]);
      
    //printf("%d %d\n", n, m);
    //for (int i=0; i<n; i++) printf("%s\n", a[i]);
    
    bool fail = false;
    for (int i=0; i<n && !fail; i++)
      for (int j=0; j<m && !fail;j++)
        if (a[i][j] == '#'){
          bool ok = fill(i, j);
          if (!ok)
            fail = true;
        }
          
      
    printf("Case #%d:\n", ++ca);
    if (fail)
      printf("Impossible\n");
    else{
      for (int i=0; i<n; i++)
        printf("%s\n", a[i]);
    }    
  }
  return 0;
}
