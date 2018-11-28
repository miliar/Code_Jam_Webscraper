// C small CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define oo 1000000000
const static int maxN = 1000;

int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);
    int T;
    int N;
    int tmp;
    int i;
    int ans, sum, minval;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &N);
        ans = sum = 0;
        minval = oo;
        for (i = 0; i < N; i++)
        {
            scanf("%d", &tmp);
            ans ^= tmp;
            sum += tmp;
            minval = min(minval, tmp);
        }
        if (ans)
        {
            printf("Case #%d: NO\n", cas++);
        }
        else
        {
            printf("Case #%d: %d\n", cas++, sum - minval);
        }
    }
    return 0;
}
