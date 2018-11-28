#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

const int N=1001;

char a[N],c[N];
int n,m,use[5],p[5],ans;

void dfs(int pos)
{
     int i,j;
     if (pos>=m)
     {
        for (i=0;i<n;i+=m)
            for (j=0;j<m;j++) c[i+j]=a[i+p[j]];
        c[n]=0;
        j=1;
        for (i=1;i<n;i++)
        if (c[i]!=c[i-1]) j++;
        if (j<ans) ans=j;
        return ;
     }
     for (i=0;i<m;i++)
     if (use[i]==0)
     {
        use[i]=1;
        p[pos]=i;
        dfs(pos+1);
        use[i]=0;
     }
}
int main()
{
    int test,ncase=1,i,j,k;
    freopen("Dsmall.in","r",stdin);
    freopen("Dsmall.out","w",stdout);
    scanf("%d",&test);
    while (ncase<=test)
    {
       scanf("%d",&m);
       scanf("%s",a);
       n=strlen(a);
       ans=10000000;
       dfs(0);
       printf("Case #%d: %d\n",ncase++,ans);
    }
    return 0;
}
