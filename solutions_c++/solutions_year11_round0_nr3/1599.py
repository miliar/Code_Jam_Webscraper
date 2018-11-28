/*
 * Author: ahxgw
 * Created Time:  2011-5-7 12:54:53
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

const int MaxN = 1000010;

int T, N;
int c[MaxN];

int main()
{
    freopen("C.out", "w", stdout);
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++)
    {
        scanf("%d", &N);
        int flag = 0;
        int sum = 0;
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &c[i]);
            flag ^= c[i];
            sum += c[i];
        }
        if (flag)
        {
            printf("Case #%d: NO\n", _);
            continue;
        }
        sort(c, c + N);
        printf("Case #%d: %d\n", _, sum - c[0]);
    }

    return 0;
}
