#include<iostream>
#include<string.h>
#include<stdio.h>
#include<queue>
#include<algorithm>
using namespace std;
struct node
{
    long long x,y;
};
long long a[20];
bool xxoo[10001];
bool ooxx[1000001];
int i,j,k,n,m;
int main()
{
    queue<node> q;
    int cas;
    memset(ooxx,true,sizeof(ooxx));
    ooxx[1]=false;
    for (i=2;i<=1000000;i++)
    if (ooxx[i])
    {
             for (j=2;j<=1000000/i;j++)
             ooxx[i*j]=false;
    }
    freopen("cc.in","r",stdin);
    freopen("cc.out","w",stdout);
    scanf("%d",&cas);
    for(i=1;i<=cas;i++)
    {
        int d;
        memset(xxoo,0,sizeof(xxoo));
        scanf("%d%d",&d,&k);
        int primee=1,prime,f;
        for (j=1;j<=d;j++)
        primee*=10;
        long long MM=0;
        for (j=1;j<=k;j++)
        {
            scanf("%lld",&a[j]);
            MM=max(MM,a[j]);
        }
        bool rrflag=true;
        if (k==1)
        {
           printf("Case #%d: I don't know.\n",i);
           continue;
        }
        for (prime=max(MM+1,(long long )1);prime<=primee;prime++)
        {
            if (!ooxx[prime])continue;
            while (!q.empty())
            q.pop();
            for (j=0;j<prime;j++)
            {
                node tmp;
                tmp.x=j;
                long long tt=a[2]-a[1]*j%prime;
                tt=(tt%prime+prime)%prime;
                tmp.y=tt;
                q.push(tmp);
            }
            for (j=2;j<k;j++)
            {
            m=q.size();
            for (int r=1;r<=m;r++)
            {
                node tmp;
                tmp=q.front();
                q.pop();
                if ((a[j]*tmp.x+tmp.y)%prime==a[j+1])
                q.push(tmp);
            }
        }
        m=q.size();
        if (m==0)
        continue;
        node tmp;
        tmp=q.front();
        long long qwe=(a[k]*tmp.x+tmp.y)%prime;
        q.pop();
        bool flag=true;
        for (j=2;j<=m;j++)
        {
            tmp=q.front();
            q.pop();
            if ((a[k]*tmp.x+tmp.y)%prime!=qwe)
            flag=false;
        }
        if (flag)
        {
           xxoo[qwe]=true;
        }
        else
        {
            continue;
        }
    }
    int ew=-1;
    for (j=0;j<primee;j++)
    if (xxoo[j]&&ew==-1)
    ew=j;
    else if (xxoo[j]){
    ew=-1;break;}
    if (ew==-1)
    {
         printf("Case #%d: I don't know.\n",i);
    }
    else 
      printf("Case #%d: %d\n",i,ew);}
}
               
        
