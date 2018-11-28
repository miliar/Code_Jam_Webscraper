#include <stdio.h>
#include <string.h>
#include <algorithm>
#define MaxN 14
#define two(v) (1<<(v))
using namespace std;
int dp[two(MaxN)][MaxN], m[two(MaxN)], v[two(MaxN)], T, p;

void update(int &x, int y)
{
    if (y < x) x = y;
}

void dfs(int x)
{
    if (x >= two(p)) {
        dp[x][m[x-two(p)]] = 0;
        return;
    }
    dfs(2*x);
    dfs(2*x+1);
    for (int i = 0; i <= p; ++i)
        for (int j = 0; j <= p; ++j) {
            update(dp[x][max(i, j)], dp[2*x][i]+dp[2*x+1][j]);
            if (max(i, j) > 0) update(dp[x][max(i, j) - 1], dp[2*x][i]+dp[2*x+1][j]+v[x]);
        }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        memset(dp, 0x3f, sizeof(dp));
        scanf("%d", &p);
        for (int i = 0; i < two(p); ++i) {
            scanf("%d", &m[i]);
            m[i] = p-m[i];
        }
        for (int i = 1; i <= p; ++i) {
            int off = two(p-i);
            for (int j = 0; j < off; ++j)
                scanf("%d", &v[off+j]);
        }
        dfs(1);
        printf("Case #%d: %d\n", cas, dp[1][0]);
    }
    return 0;
}

//#include <stdio.h>
//#include <algorithm>
//#define MaxN 14
//#define two(v) (1<<(v))
//using namespace std;
//
//int p, s[two(MaxN)], ans, T, v[two(MaxN)];
//
//void dfs(int x)
//{
//    if (x >= two(p)) return;
//    dfs(2*x);
//    dfs(2*x+1);
//    s[x] = max(s[2*x], s[2*x+1]);
//}
//
//void dfs2(int x, int cnt)
//{
//    if (s[x] <= 0) return;
//    ++ans; ++cnt;
//    s[2*x] -= cnt;
//    s[2*x+1] -= cnt;
//    dfs2(2*x, cnt);
//    dfs2(2*x+1, cnt);
//}
//
//int main()
//{
//    //freopen("test.txt", "r", stdin);
//    freopen("B-small-attempt1.in", "r", stdin);
//    freopen("B-small-attempt1.out", "w", stdout);
//    scanf("%d", &T);
//    for (int cas = 1; cas <= T; ++cas) {
//        ans = 0;
//        scanf("%d", &p);
//        for (int i = 0; i < two(p); ++i) {
//            scanf("%d", &s[two(p)+i]);
//            s[two(p)+i] = p-s[two(p)+i];
//        }
//        for (int i = 1; i <= p; ++i) {
//            int off = two(p-i);
//            for (int j = 0; j < off; ++j)
//                scanf("%d", &v[off+j]);
//        }
//        dfs(1);
//        dfs2(1, 0);
//        printf("Case #%d: %d\n", cas, ans);
//    }
//    return 0;
//}
