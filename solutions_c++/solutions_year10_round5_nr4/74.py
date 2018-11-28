#include <cstdio>
#include <iostream>
#include <cstring>
#define MAXB 10
using namespace std;

char used[MAXB+1][MAXB+1];
int seq[MAXB+1];
int n,b,ans;

int check(int x)
{
    int i;
    for(i=0;x!=0;i++)
    {
        if(used[i][x%b]==1)
        {
            return 0;
        }
        x=x/b;
    }
    return 1;
}

void put(int x)
{
    int i;
    for(i=0;x!=0;i++)
    {
        used[i][x%b]=1;
        x=x/b;
    }
}

void unput(int x)
{
    int i;
    for(i=0;x!=0;i++)
    {
        used[i][x%b]=0;
        x=x/b;
    }
}

void backtrack(int k,int p,int s)
{
    int i;
    if(s==n)
    {
        ans++;
        return;
    }
    if(k>=b)
    {
        return;
    }
    for(i=p;s+i<=n;i++)
    {
        if(check(i)==1)
        {
            seq[k]=i;
            put(i);
            backtrack(k+1,i+1,s+i);
            unput(i);
        }
    }
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int c,t;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d",&n,&b);
        memset(used,0,sizeof(used));
        ans=0;
        backtrack(0,1,0);
        printf("Case #%d: %d\n",c+1,ans);
    }
    return 0;
}
