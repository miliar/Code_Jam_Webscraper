#include <cstdio>
#include <string>
#include <stdlib.h>
#include <algorithm>
using namespace std;

const int maxn = 500;

bool x[maxn],y[maxn];
int n,m,casen,T,h,Min,l,i,j,na,nb;
int abc[500],def[500],e[500][500],Link[500];

bool check(int x)
{
     int i,v;
     
     for (i=1;i<=e[x][0];i++)
     {
         v = e[x][i];
         if (y[v]==false)
         {
            y[v] = true;
            if (Link[v]==0 || check(Link[v])) { Link[v] = x; return true; }
         }
     }
     return false;
} 

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &casen);
    for (l=1;l<=casen;l++)
    {
        scanf("%d",&T);
        scanf("%d%d",&n,&m);
        for (i=1;i<=n+m;i++)
        {
            scanf("%d:%d",&h,&Min); abc[i] = h * 60 + Min;
            scanf("%d:%d",&h,&Min); def[i] = h * 60 + Min;
        }
        memset(e,0,sizeof(e));
        for (i=1;i<=n;i++)
        {
            for (j=n+1;j<=n+m;j++)
            {
                if (def[i]+T<=abc[j]) { e[i][0] ++; e[i][e[i][0]] = j; }
                if (def[j]+T<=abc[i]) { e[j][0] ++; e[j][e[j][0]] = i; }
            }
        }
        
        memset(Link,0,sizeof(Link));
        na = 0; nb = 0;
        for (i=1;i<=n+m;i++) { memset(y,0,sizeof(y)); check(i); }
        for (i=1;i<=n;i++) if (Link[i]==0) na ++;
        for (i=n+1;i<=n+m;i++) if (Link[i]==0) nb ++;
        printf("Case #%d: %d %d\n",l,na,nb);
    }
    return 0;
}
