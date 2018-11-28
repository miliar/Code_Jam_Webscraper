#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

const int MAXN = 305;


int flag[MAXN],but[MAXN];
int p[2][2];

void work(int i,int &ans)
{
    if(but[i] >= p[flag[i]][0] && but[i] <= p[flag[i]][1])
    {
        ans += 1;
        p[flag[i]][0] = p[flag[i]][1] = but[i];
        p[flag[i]^1][0] -= 1;
        p[flag[i]^1][1] += 1;
    }
    else if(but[i] < p[flag[i]][0])
    {
        int t = p[flag[i]][0] - but[i] + 1;
        ans += t;
        p[flag[i]][0] = p[flag[i]][1] = but[i];
        p[flag[i]^1][0] -= t;
        p[flag[i]^1][1] += t;
    }
    else
    {
        int t = but[i] - p[flag[i]][1] + 1;
        ans += t;
        p[flag[i]][0] = p[flag[i]][1] = but[i];
        p[flag[i]^1][0] -= t;
        p[flag[i]^1][1] += t;
    }
}

int main()
{
    freopen("aaa.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k;
    int t,n;
    char s[5];
    scanf("%d",&t);
    for(k = 1;k <= t;k ++)
    {
        scanf("%d",&n);
        for(i = 1;i <= n;i ++)
        {
            scanf("%s%d",s,&but[i]);
            if(s[0] == 'B') flag[i] = 0;
            else flag[i] = 1;
        }
        int ans = 0;
        p[0][0] = p[1][1] = p[0][1] = p[1][0] = 1;
        for(i = 1;i <= n;i ++)
        {
            work(i,ans);
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
