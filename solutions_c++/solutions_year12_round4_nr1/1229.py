#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <queue>

#define MAXN 10100
using namespace std;
int CAS,n;
int di[MAXN],li[MAXN],D;
long long dp[MAXN];
struct mode
{
    int sum,value;
};
bool operator < (const mode &a,const mode &b)
    {
        return a.value > b.value;
    }
priority_queue<mode> Queue;

long long minx(long long  a,long long b)
{
    return a < b ? a : b;
}
long long maxx(long long a,long long b)
{
    return a > b ? a : b;
}
int main()
{
    Queue.push(mode{1,2});
    Queue.push(mode{2,3});
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&CAS);
    for(int cas = 1;cas <= CAS;cas++)
    {
        memset(dp,0,sizeof dp);
        scanf("%d",&n);
        for(int i = 0;i < n;i++)
            scanf("%d%d",&di[i],&li[i]);
        scanf("%d",&D);
        while(!Queue.empty())
            Queue.pop();
        dp[0] = minx(li[0],di[0]);
        Queue.push(mode{dp[0]+di[0],di[0]});
        for(int i = 1;i < n;i++)
        {
            mode tmp;
            while(!Queue.empty())
            {
                tmp = Queue.top();
                if(tmp.sum >= di[i])
                    break;
                Queue.pop();
            }
            //printf("%d %d\n",tmp.value.first,Queue.top().second);
            if(Queue.empty())   break;
            dp[i] = minx(li[i],di[i] - tmp.value);
            Queue.push(mode{di[i]+dp[i],di[i]});
        }
        //printf("D:%d\n",D);
        bool f = false;
        for(int i = 0;i < n;i++)
        {
            //printf("%d %d\n",dp[i],di[i]);
            if(dp[i] >= D - di[i])
                f = true;
        }
        printf("Case #%d: ",cas);
        if(f) printf("YES\n");
        else printf("NO\n");
    }
    fclose(stdin);
    fclose(stdout);
}
