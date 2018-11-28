/*
 * Author: ahxgw
 * Created Time:  2011-5-21 9:15:35
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) fprintf(stderr, "%s: %I64d\n", #v, (long long)(v))
#define SZ(v) ((int)(v).size())
#define p_b push_back
#define m_p make_pair
const int maxint = -1u>>1;
template<class T> void toMax(T &a, T b) {if (b > a) a = b;}
template<class T> void toMin(T &a, T b) {if (b < a) a = b;}

typedef long long LL;

int T, pD, pG;
LL N;
bool ans;

int main()
{
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++)
    {
        ans = 0;
        scanf("%lld%d%d", &N, &pD, &pG);
        if (pG == 100 && pD != 100)
            ans = 0;
        else if (pD && pG == 0)
            ans = 0;
        else if (pD == 0)
            ans = 1;
        else if (N >= 100)
            ans = 1;
        else
        {
            for (int i = 1; i <= N; i++)
            {
                if (i * pD % 100 == 0)
                {
                    ans = 1;
                    break;
                }
            }
        }
        printf("Case #%d: %s\n", _, ans ? "Possible" : "Broken");
    }

    return 0;
}
