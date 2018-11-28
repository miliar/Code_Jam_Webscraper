// C CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define PI acos(-1.0)
#define eps 1e-5
#define oo 10000000000000000LL
const static int maxN = 10000;
typedef long long INT64;

int a[maxN];

bool harmonious(int& N, int f)
{
    int i;
    for (i = 0; i < N; i++)
    {
        if (f % a[i] == 0 || a[i] % f == 0)
        {
        }
        else
        {
            return false;
        }
    }
    return true;
}

int calc(int& N, int& L, int& H)
{
    int i;
    for (i = L; i <= H; i++)
    {
        if (harmonious(N, i))
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);
    int T;
    int cas = 1;
    int N, L, H;
    int i;
    int ans;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d%d\n", &N, &L, &H);
        for (i = 0; i < N; i++)
        {
            scanf("%d", &a[i]);
        }
        ans = calc(N, L, H);
        if (ans == -1)
        {
            printf("Case #%d: NO\n", cas++);
        }
        else
        {
            printf("Case #%d: %d\n", cas++, ans);
        }
    }
    return 0;
}
