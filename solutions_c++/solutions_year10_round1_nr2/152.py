#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>

#define INF 1000000000
#define MAXX 256

using namespace std;

int t,iii,i,j,k;
int n,d,in,m,a[305];
int mic[305][305];
int ans;
int cnt;

inline int abb(int u)
{
    if(u>0)
    return u;
    else
    return -u;
}

int val(int l)
{
    if(l<0)
    return 0;
    else
    return l;
}

int main()
{
    scanf("%d",&t);
    for(iii=1;iii<=t;iii++)
    {
        scanf("%d %d %d %d",&d,&in,&m,&n);
        ans=INF;
        for(i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
        }
        for(i=1;i<=n;i++)
        {
            for(j=0;j<=MAXX;j++)
            {
                mic[i][j]=d+mic[i-1][j];
                for(k=0;k<=MAXX;k++)
                {
                    if(m!=0)
                    {
                        if(mic[i][j]>mic[i-1][k]+abb(j-a[i])+in*(val(abb(k-j)-1)/m))
                        {
                            mic[i][j]=mic[i-1][k]+abb(j-a[i])+in*(val(abb(k-j)-1)/m);
                        }
                    }
                    else
                    {
                        if(k==j&&mic[i][j]>mic[i-1][k]+abb(j-a[i]))
                        {
                            mic[i][j]=mic[i-1][k]+abb(j-a[i]);
                        }
                    }
                }
            }
        }
        for(j=0;j<=MAXX;j++)
        {
            if(mic[n][j]<ans)
            ans=mic[n][j];
        }
        printf("Case #%d: %d\n",iii,ans);
    }
    return 0;
}
