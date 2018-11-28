#include <stdio.h>
#include <string.h>

#define N 19
char w[]="welcome to code jam";

int main(){
  int n; scanf("%d",&n);
  char s[1000];
  gets(s);
  int f[1000][N], g[1000][N];
  for (int ti=1;ti<=n;ti++){
    gets(s);
    //printf("%s | %s\n",s,w);
    int m = strlen(s);
    memset(f,0,sizeof(f));
    memset(g,0,sizeof(g));
    if (s[0]==w[0]){
      f[0][0]=1;
      g[0][0]=1;
    }

    for (int i=1;i<m;i++){
      if (s[i]==w[0]){
        f[i][0]=1;
      }
      g[i][0]=(g[i-1][0]+f[i][0])%1000;
      for (int j=1;j<N && j<=i;j++){
        //printf("%d %d : %c %c\n",i,j,s[i],w[j]);
        if (s[i]==w[j]){
          f[i][j]=g[i-1][j-1];
        }else{
          f[i][j]=0;
        }
        g[i][j]=(g[i-1][j]+f[i][j])%1000;
      }
    }
    /*
    for (int i=0;i<m;i++)printf("  %c ",s[i]); puts("");
    for (int i=0;i<N;i++){
      for (int j=0;j<m;j++)printf("%3d ",g[j][i]);
      puts("");
    }
    */

    printf("Case #%d: %04d\n",ti,g[m-1][N-1]);
  }

  return 0;
}
