#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <cstring>
#include <queue>
using namespace std;

const int MAXN = 2100, INF = 1000000000;
int N, themax[MAXN], h[MAXN];
bool flag;

void solve(int now)
{
    if(flag) return ;
    if(now == 0)
    {
        for(int i = 1; i <= N; i++)
            printf(" %d", h[i]);
        printf("\n");
        flag = true;
        return ;
    }

    for(int i = N+3; i >= 0; i--)
    {
        h[now] = i;
        if(now != N)
        {
            int tmax = -1, tindex = 0, small = 0;

            for(int j = now+1; j <= N; j++)
            {
                if(tmax == -1 || (tmax == 0 && (tindex-now) * (h[j]-h[now]) > (j-now) * (h[tindex]-h[now])))
                    tmax = 0, tindex = j;
                //if(h[j] >= h[now]) small = 1;
            }
            //special case
            /*if(small==0)
            {
                tmax = -1;
                for(int j = now+1; j <= N; j++)
                    if(h[j] > tmax)
                        tmax = h[j], tindex = j;
            }*/                

            if(tindex == themax[now]) solve(now-1);        
        }
        else solve(now-1);
    }
    
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; T--; t++)
    {
        memset(h, 0, sizeof(h));
        bool negcyc = false;
        scanf("%d", &N);

        for(int i = 1; i < N; i++)
            scanf("%d", &themax[i]);
        flag = false;
        printf("Case #%d:", t);
        solve(N);
        if(!flag) printf(" Impossible\n");
    }
    return 0;
}
