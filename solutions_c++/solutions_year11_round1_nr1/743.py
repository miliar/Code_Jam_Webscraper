// A CZM1.0
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
#define oo 0x3f3f3f3f
const static int maxN = 1000 + 1;
typedef long long INT64;

INT64 gcd(INT64 a, INT64 b)
{
    if (!b) return a;
    return gcd(b, a % b);
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T;
    INT64 N;
    INT64 PD, PG;
    int cas = 1;
    bool flag;
    INT64 t;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%I64d%I64d%I64d", &N, &PD, &PG);
        flag = true;
        if (PD)
        {
            t = gcd(PD, 100);
            if (100 / t > N)
            {
                flag = false;
            }
        }
        if (PG == 100 && PD != 100)
        {
            flag = false;
        }
        if (PG == 0 && PD != 0)
        {
            flag = false;
        }
        printf("Case #%d: %s\n", cas++, flag ? "Possible" : "Broken");
    }
    return 0;
}
