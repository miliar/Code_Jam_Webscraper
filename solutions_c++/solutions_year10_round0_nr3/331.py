#include<iostream>
using namespace std;
const int maxn=1010;
typedef long long ll;
int cases,t,n,lim,turn,a[maxn],next[maxn],sum[maxn],vis[maxn];
ll sum1[maxn],ans;
void init()
{
     scanf("%d%d%d",&turn,&lim,&n);
     int i;
     for (i=0;i<n;i++) scanf("%d",&a[i]);
}

void work()
{
     int s,i,j;
     ll s1;
     for (i=0;i<n;i++)
     {
         s=0;
         j=i;
         while (1)
         {
             if (s+a[j]>lim) break;
             s+=a[j];
             j++;
             if (j==n) j=0;
             if (j==i) break;
         }
         next[i]=j;
         sum[i]=s;
     }     
     memset(vis,0,sizeof(vis));
     i=0;
     j=0;
     s1=0;
     ans=0;
     while (1)
     {
          if (vis[i])
          {
             s1=s1-sum1[i];
             if (turn>=vis[i])
             {
             turn-=vis[i];
             ans=s1*(turn/(j-vis[i]));
             turn%=j-vis[i];
             ans+=sum1[i];
             while (turn>0)
             {
                   turn--;
                   ans+=sum[i];
                   i=next[i];
             }
             }
             else
             {
                 i=0;
             while (turn>0)
             {
                   turn--;
                   ans+=sum[i];
                   i=next[i];
             }
             }
             break;
          }
          sum1[i]=s1;
          vis[i]=j;
          s1+=sum[i];
          i=next[i];
          j++;
     }
}

void print()
{
     printf("Case #%d: %lld\n",t+1,ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),t=0;t<cases;t++)
    {
        init();
        work();
        print();
    }
    return 0;
}
