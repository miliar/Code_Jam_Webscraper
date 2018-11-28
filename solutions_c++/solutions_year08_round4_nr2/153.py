#include<iostream>
using namespace std;
const int maxn=100;
int test,tt,wt,na,nb,ta1[maxn],ta2[maxn],tb1[maxn],tb2[maxn],g[maxn][maxn],p[maxn],v[maxn];
void init()
{
     scanf("%d",&wt);
     scanf("%d%d",&na,&nb);
     int i,x,y;
     for (i=0;i<na;i++)
     {
         scanf("%d:%d",&x,&y);
         ta1[i]=x*60+y;
         scanf("%d:%d",&x,&y);
         ta2[i]=x*60+y;
     }
     for (i=0;i<nb;i++)
     {
         scanf("%d:%d",&x,&y);
         tb1[i]=x*60+y;
         scanf("%d:%d",&x,&y);
         tb2[i]=x*60+y;
     }
}

int go(int x)
{
    int i,tmp;
    for (i=0;i<nb;i++)
    if ((g[x][i])&&(!v[i]))
    {
       v[i]=1;
       tmp=p[i];
       p[i]=x;
       if ((tmp==-1)||(go(tmp))) return 1;
       p[i]=tmp;
    }
    return 0;
}

void work()
{
     int i,j,ans;
     memset(g,0,sizeof(g));
     for (i=0;i<na;i++)
         for (j=0;j<nb;j++)
         if (ta1[i]>=tb2[j]+wt) g[i][j]=1;
     memset(p,-1,sizeof(p));
     for (i=0,ans=na;i<na;i++)
     {
         memset(v,0,sizeof(v));
         if (go(i)) ans--;
     }
     printf(" %d",ans);
}

void print()
{
     int i;
     printf("Case #%d:",tt);
     work();
     for (i=0;i<max(na,nb);i++) 
     {
         swap(ta1[i],tb1[i]);
         swap(ta2[i],tb2[i]);
     }
     swap(na,nb);
     work();
     printf("\n");
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&test);
    for (tt=1;tt<=test;tt++)
    {
        init();
        print();
    }
    return 0;
}
