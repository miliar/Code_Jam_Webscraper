#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
const int maxm = 10000000;
const int maxn = 10000+5;
struct Edge
{
    int next,v;
};
struct node
{
    int x,y;
};
Edge e[maxm];
node a[maxn];
int head[maxn];
int n,m,eid;
int d;
int flag;
void dfs(int x,int l)
{
   // printf("%d %d\n",x,l);
    if (flag==1) return;
    if (a[x].x+l>=d)
    {
            flag=1;
            return;
    }

    for (int i=x+1;i<n;i++)
    {
     //printf("%d\n",a[i].x);
        if (a[x].x+l>=a[i].x)
        {
            dfs(i,min(a[i].x-a[x].x,a[i].y));
        }
        else break;
    }
    return;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int i,j,t,ca=0;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%d%d",&a[i].x,&a[i].y);
        }
        scanf("%d",&d);
        flag = 0;
       // printf("n = %d\n",n);
        dfs(0,min(a[0].x,a[0].y));
        if (flag) printf("Case #%d: YES\n",++ca);
        else printf("Case #%d: NO\n",++ca);
    }
    return 0;
}
