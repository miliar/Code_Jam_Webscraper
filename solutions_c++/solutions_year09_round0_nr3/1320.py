#include <cstdio>
#include <cstring>

const int M = 1000;
const int MOD = 10000;

char a[M];
char b[]="welcome to code jam";
int m,n;

int dyn[M][M];

void dynamik() {
  for(int i=1;i<=n;++i) dyn[0][i]=0;
  dyn[0][0]=1;
  for(int i=1;i<=m;++i) {
    dyn[i][0]=1;
    for(int j=1;j<=n;++j) {
      dyn[i][j]=dyn[i-1][j];
      if(a[i-1]==b[j-1]) {
        dyn[i][j]+=dyn[i-1][j-1];
        dyn[i][j]%=MOD;
      }
    }
  }
}

int main() {
  int d;
  n=strlen(b);
  scanf("%d\n", &d);
  for(int i=1; i<=d; ++i) {
    gets(a);
    scanf("\n");
    m=strlen(a);
    dynamik();
    printf("Case #%d: %04d\n", i, dyn[m][n]);
  }
}