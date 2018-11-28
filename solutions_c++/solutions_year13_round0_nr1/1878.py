#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<deque>
#include<map>
#include<set>
#include<cstdlib>
#include<string>

#define ls (v<<1)
#define rs (v<<1|1)
#define lowbit (v&-v)
#define PI (acos(-1.0))
#define FOR(i,n) ((i)=0;i<(n);(i)++)
#define FOR1(i,n) ((i)=1;i<=(n);(i)++)
#define INF (0x7fffffff)
#define INFL (0x7fffffffffffffffll)
#define MAXN  0

using namespace std;


char mp[4][5];

int getResult()
{
    int i,j,r=0;
    for(i=0;i<4;i++)
    {
        scanf("%s",mp[i]);
        for(j=0;j<4;j++)
        {
            if(mp[i][j]=='.')
            {
                r=1;
            }
        }
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(mp[i][j]=='X' || mp[i][j]=='.')
            {
                break;
            }
        }
        if(j>=4)
        {
            return 2;
        }
        for(j=0;j<4;j++)
        {
            if(mp[j][i]=='X' || mp[j][i]=='.')
            {
                break;
            }
        }
        if(j>=4)
        {
            return 2;
        }
    }
    for(i=0;i<4;i++)
    {
        if(mp[i][i]=='.' || mp[i][i]=='X')
        {
            break;
        }
    }
    if(i>=4)
    {
        return 2;
    }
    for(i=0;i<4;i++)
    {
        if(mp[i][3-i]=='.' || mp[i][3-i]=='X')
        {
            break;
        }
    }
    if(i>=4)
    {
        return 2;
    }



    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(mp[i][j]=='O' || mp[i][j]=='.')
            {
                break;
            }
        }
        if(j>=4)
        {
            return 3;
        }
        for(j=0;j<4;j++)
        {
            if(mp[j][i]=='O' || mp[j][i]=='.')
            {
                break;
            }
        }
        if(j>=4)
        {
            return 3;
        }
    }
    for(i=0;i<4;i++)
    {
        if(mp[i][i]=='.' || mp[i][i]=='O')
        {
            break;
        }
    }
    if(i>=4)
    {
        return 3;
    }
    for(i=0;i<4;i++)
    {
        if(mp[i][3-i]=='.' || mp[i][3-i]=='O')
        {
            break;
        }
    }
    if(i>=4)
    {
        return 3;
    }
    return r;
}

int main()
{
    freopen("A-large.out","w",stdout);
    freopen("A-large.in","r",stdin);
    int t,cas=1;
    int w;
    scanf("%d",&t);
    while(t--)
    {
        w=getResult();
        printf("Case #%d: ",cas++);
        if(w==0)
        {
            puts("Draw");
        }
        else if(w==1)
        {
            puts("Game has not completed");
        }
        else if(w==2)
        {
            puts("O won");
        }
        else
        {
            puts("X won");
        }
    }


    return 0;
}
