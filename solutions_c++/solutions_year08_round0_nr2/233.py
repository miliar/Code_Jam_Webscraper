#include <cstdio>
#include <iostream>
#include <algorithm>
#define MAXM 200
using namespace std;

struct Table
{
    int x;
    int y;
    int t;
}table[MAXM+1];

int cnt[2];
int n,m,t,na,nb;

bool operator<(const Table &a,const Table &b)
{
    if((a.x<b.x)||((a.x==b.x)&&(a.y<b.y)))
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k,h1,m1,h2,m2,prev,start;
    bool change;
    scanf("%d",&n);
    for(k=0;k<n;k++)
    {
        scanf("%d",&t);
        scanf("%d %d",&na,&nb);
        m=0;
        for(i=0;i<na;i++)
        {
            scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
            table[m].x=60*h1+m1;
            table[m].y=60*h2+m2;
            table[m].t=0;
            m++;
        }
        for(j=0;j<nb;j++)
        {
            scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
            table[m].x=60*h1+m1;
            table[m].y=60*h2+m2;
            table[m].t=1;
            m++;
        }
        sort(table,table+m);
        cnt[0]=cnt[1]=0;
        do
        {
            change=false;
            prev=-1;
            start=0;
            for(i=0;i<m;i++)
            {
                if((table[i].t<2)&&(table[i].t!=prev)&&(table[i].x>=start))
                {
                    change=true;
                    if(prev==-1)
                    {
                        cnt[table[i].t]++;
                    }
                    prev=table[i].t;
                    start=table[i].y+t;
                    table[i].t=table[i].t+2;
                }
            }
        }while(change==true);
        printf("Case #%d: %d %d\n",k+1,cnt[0],cnt[1]);
    }
    return 0;
}
