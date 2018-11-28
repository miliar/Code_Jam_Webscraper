#include <cstdio>
#include <cstdlib>
int N,M,s;

int Min(int a,int b)
{
    return a < b?a:b;
}

bool check(int x1,int y1,int x2,int y2)
{
    if (abs(x1 * y2 - x2 * y1) != s)
        return false;
    if (abs(x2 - x1) > N || abs(x2) > N || abs(x1) > N)
        return false;
    if (abs(y2 - y1) > M || abs(y2) > M || abs(y1) > M)
        return false;
    int x = -Min(x1,x2);
    int y = -Min(y1,y2);
    if (x < 0)
        x = 0;
    if (y < 0)
        y = 0;
    printf("%d %d %d %d %d %d\n",x1+x,y1+y,x,y,x2+x,y2+y);
    return true;
}

void work()
{
    scanf("%d%d%d",&N,&M,&s);
        for (int x1 = -N; x1 <= N; ++x1)
            for (int x2 = x1; x2 <= Min(N,x1 + N); ++x2)
                for (int y1 = -M; y1 <= M; ++y1)
                    for (int y2 = y1; y2 <= Min(M,y1 + M); ++y2)
                        if (check(x1,y1,x2,y2))
                            return;
                        else if (check(x1,y2,x2,y1))
                            return;
    printf("IMPOSSIBLE\n");
}
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        printf("Case #%d: ",T);
        work();
    }
    return 0;
}
