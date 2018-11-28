#include<iostream>
#include<cmath>
using namespace std;
int x1, Y1, x2, y2, N, M, A;
bool Solve()
{
    int S, ma;
    for(x1 = 0; x1 <= N; ++x1)
    {
        for(y2 = 0; y2 <= M; ++y2)
        {
            S = A + y2 * x1;
            ma = sqrt(S);
            for(x2 = 1; x2 <= ma; ++x2)
                if(S % x2 == 0)
                {
                    Y1 = S / x2;
                    if(Y1 <= M && x2 <= N)
                        return 1;
                    else if(Y1 <= N && x2 <= M)
                    {
                         swap(Y1, x2);
                         return 1;
                    }
                }
        }
    }
    return 0;
}
int main()
{
    int t, i;
    freopen("B_S2.in", "r", stdin);
    freopen("B_S2.out", "w", stdout);
    scanf("%d", &t);
    for(i = 1; i <= t; ++i)
    {
        scanf("%d%d%d", &N, &M, &A);
        printf("Case #%d:", i);
        if(Solve()) printf(" 0 0 %d %d %d %d\n", x1, Y1, x2, y2);
        else printf(" IMPOSSIBLE\n");
    }
}
