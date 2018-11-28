// Robots.cpp

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _DEBUG
#define ASSERT(x)  {if(!(x)) __asm{int 3};}
#else
#define ASSERT(x)  do{}while(0)
#endif
typedef long long LONG;

#define MAXN 1000
int edge[MAXN+1];
bool vis[MAXN+1];

void reset()
{
    memset(edge, 0, sizeof(edge));
    memset(vis, 0, sizeof(vis));
}

int dfs(int i)
{
    int count = 0;
    int j = i;
    while(!vis[i])
    {
        ++count;
        vis[i] = true;
        ASSERT(edge[i] > 0);
        i = edge[i];
    }
    ASSERT(j == i);
    return count;
}

int solve(int n)
{
    int i;
    int subg = 0;
    int x = 0;
    int cycle;
    for(i = 1; i<=n; i++)
    {
        if(!vis[i])
        {
            cycle = dfs(i);
            if(cycle > 1)
                x += cycle;
        }
    }
    return x;
}

int main(int argc, const char* argv[])
{
    int T = 0 ,N = 0;
    int i;
    int ret;
    int caseIndex = 1;
    ret = scanf("%d", &T);
    ASSERT(ret != EOF && T > 0 && T<=100);
    while(T--)
    {
        reset();
        scanf("%d", &N);
        for( i = 1; i<=N; i++)
            scanf("%d", &edge[i]);
        int x = solve(N);

#ifdef _DEBUG_X
        for(i = 1; i <= N; i++)
            printf("%d ", edge[i]);
#endif
        printf("Case #%d: %.6f\n", caseIndex++, (double)x);

    }
	return 0;
}

