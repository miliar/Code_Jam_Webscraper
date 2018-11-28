#include<stdio.h>
#include<memory.h>
int W, H, R, F[128][128], a, b;
bool map[128][128];
bool Cal(int &ta, int &tb, int h, int w)
{
    ta = (2 * w - h - 1);
    tb = (2 * h - w - 1);
    if(ta % 3 || tb % 3) return 0;
    ta /= 3;
    tb /= 3;
    return 1;
}
int Solve()
{
    int A, B;
    if(!Cal(A, B, H, W)) return 0;
    int i, j;
    if(map[0][0]) return 0;
    for(i = 0; i <= B; ++i)
        for(j = 0; j <= A; ++j)
            if(i || j)
            {
                if(map[i][j] == 0)
                {
                    if(i) F[i][j] += F[i - 1][j];
                    if(j) F[i][j] += F[i][j - 1];
                    F[i][j] %= 10007;
                }
                else F[i][j] = 0;
            }
    return F[B][A];
            
}
int main()
{
    int t, ctr = 0, t1, t2, r, c;
    freopen("D_S.in", "r", stdin);
    freopen("D_S.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &H, &W, &R);
        memset(F, 0, sizeof(F));
        F[0][0] = 1;
        memset(map, 0, sizeof(map));
        while(R--)
        {
            scanf("%d%d", &r, &c);
            if(Cal(t1, t2, r, c))
                map[t2][t1] = 1;
        }
        printf("Case #%d: %d\n", ++ctr, Solve());
    }
}
