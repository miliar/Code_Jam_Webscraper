#include <stdio.h>
#include <algorithm>
#include <string.h>
#define maxn 105

using namespace std;

int pr[maxn][maxn];
int inter[maxn][maxn];
int t[maxn];
int n,m;
int tn,cp;
int ans;
int g[1<<17];
int sign(int x){
    if (x>0) return 1;else return -1;
}
int check(int x,int y){
    int i;
    for (i=0;i<m;i++)
        if (pr[x][i]==pr[y][i]) return 1;
    for (i=0;i<m-1;i++)
        if (sign(pr[x][i]-pr[y][i])*sign(pr[x][i+1]-pr[y][i+1])==-1) return 1;
    return 0;
}
int f(int ss,int k,int p){
    if (k==-1){
       if (g[ss]==-1){
          if (ss==0) g[ss]=0;else{
             g[ss]=10000;
             int i;
             for (i=0;i<n;i++)
                 if ((ss&(1<<i))>0){
                    f(ss,i,1<<i);
                    break;
                 }
          }
       }
       return g[ss];
    }else{
          int i,j,tag;
        g[ss]=min(g[ss],f(ss^p,-1,0)+1);
        for (i=k+1;i<n;i++)
            if ((ss&(1<<i))>0){
               tag=1;
               for (j=0;j<i && tag;j++)
                   if ((p&(1<<j))>0 && inter[j][i]) tag=0;
               if (tag) f(ss,i,p|(1<<i));
            } 
    }
}
int main(){
    int i,j,k;
    freopen("C.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&tn);
    for (cp=1;cp<=tn;cp++){
        scanf("%d %d",&n,&m);
        for (i=0;i<n;i++)
            for (j=0;j<m;j++) scanf("%d",&pr[i][j]);
        for (i=0;i<n-1;i++)
            for (j=i+1;j<n;j++){
                inter[i][j]=check(i,j);
                inter[j][i]=inter[i][j];
            }
        memset(t,0,sizeof(t));
        memset(g,-1,sizeof(g));      
        printf("Case #%d: %d\n",cp,f((1<<n)-1,-1,0));
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
