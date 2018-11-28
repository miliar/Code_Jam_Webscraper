#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<vector>
#include<ctime>
using namespace std;
struct nod
{
    int d,l;
}node[10005];
int dis[10005];
int cmp(const void *p,const void *q)
{
    nod *a=(nod *)p;
    nod *b=(nod *)q;
    if(a->d != b->d)return a->d - b->d;
    return a->l - b->l;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,tt=0,n,i,len,flag;
    scanf("%d",&t);
    while(t--)
    {
        tt++;
        scanf("%d",&n);
        for(i=0;i<n;i++)scanf("%d%d",&node[i].d,&node[i].l);
        scanf("%d",&len);
        printf("Case #%d: ",tt);
        node[0].l=node[0].d;
        qsort(node,n,sizeof(node[0]),cmp);
        memset(dis,0,sizeof(dis));
        dis[0]=node[0].d;
        for(flag=0;flag<n;flag++)
            for(i=flag+1;i<n;i++)
            {
                if(node[flag].d+dis[flag]<node[i].d)continue;
                if(node[i].d-node[flag].d>=node[i].l && dis[i]<node[i].l)dis[i]=node[i].l;
                if(node[i].d-node[flag].d<node[i].l && dis[i]<node[i].d-node[flag].d)dis[i]=node[i].d-node[flag].d;
            }
        for(flag=0;flag<n;flag++)
            if(node[flag].d+dis[flag]>=len)
            {
                puts("YES");
                break;
            }
        if(flag==n)puts("NO");
    }
    return 0;
}
