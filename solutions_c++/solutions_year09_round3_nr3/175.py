#include <stdio.h>
#include <string.h>
#define maxn 110
int n,m;
int a[maxn];
int tn,cp;
int g[maxn][maxn];
int f(int x,int y){
    int i;
    if (g[x][y]==-1){
       if (x==y){
          g[x][y]=a[y+1]-a[x-1]-2;   
       }else{
          g[x][y]=1<<30;      
          for (i=x;i<=y;i++){
              int k=a[y+1]-a[x-1]-2;
              if (i>x) k+=f(x,i-1);
              if (i<y) k+=f(i+1,y);
              if (k<g[x][y]) g[x][y]=k;
          }   
       }
    }
    return g[x][y];
}
int main(){
    int i;
    freopen("c.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&tn);
    for (cp=1;cp<=tn;cp++){
        scanf("%d %d",&m,&n);
        a[0]=0;a[n+1]=m+1;
        for (i=1;i<=n;i++) scanf("%d",a+i);
        memset(g,-1,sizeof(g));
        printf("Case #%d: %d\n",cp,f(1,n));
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
