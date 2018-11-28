#include<stdio.h>
#include<string.h>
#define _cls(x) memset(x,0,sizeof(x))
#define MAX 510
struct rec
{
    int from,to;
    rec *next;
}edge[1000010],*map[1010];
int data[210][210];
void add(int &num,int u,int v)
{
    ++num;
    edge[num].from=u;edge[num].to=v;
    edge[num].next=map[u];map[u]=edge+num;
    //printf("%d %d\n",edge[num].from,edge[num].to);
}int match1[MAX],match2[MAX],a1[MAX],a2[MAX];
void bfs(int s)
{
     int i,j,h,t;
     rec *p;
     for (_cls(a2),a1[h=t=1]=s;h<=t && !match1[s];h++)
         for (p=map[i=a1[h]];p && !match1[s];p=p->next)
             if (!a2[j=p->to])
             {
                a1[++t]=match2[j];a2[j]=i;
                if (!a1[t])
                {
                   int temp;
                   for (temp=j;temp;j=temp)
                   {
                       match2[j]=i=a2[j];
                       temp=match1[i];
                       match1[i]=j;
                   }
                }
             }
}
int match(int n)
{
     int i,ans;
     _cls(match1);_cls(match2);
     for (ans=0,i=1;i<=n;ans+=(match1[i++]>0)) bfs(i);
     return ans;
}
int main()
{
    int t;
    freopen("C-large.in","r",stdin);
    freopen("out","w",stdout);
    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for (int i=1;i<=n;i++)
            for (int j=1;j<=k;j++)
                scanf("%d",&data[i][j]);
        int tot=0;_cls(map);
        for (int i=1;i<=n;i++)
            for (int j=1;j<=n;j++)
                if (i!=j)
                {
                    bool ok=true;
                    for (int p=1;p<=k;p++)
                        if (data[i][p]<=data[j][p])
                        {
                            ok=false;
                            break;
                        }
                    if (ok) add(tot,i,j);
                }
        printf("Case #%d: %d\n",tt,n-match(n));
    }
}