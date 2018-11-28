#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

typedef long long LL;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

int N, L, H;
int a[10000];

int main()
{
//    freopen("../DefaultProject/1.txt", "r", stdin);
    freopen("../DefaultProject/C-small-attempt0.in", "r", stdin);
    freopen("../DefaultProject/C-small-attempt0.out", "w", stdout);

    int T;
    scanf("%d", &T);
    rep(tc, T)
    {
        printf("Case #%d: ", tc + 1);

        scanf("%d%d%d", &N, &L, &H);
        rep(i, N)
        {
            scanf("%d", &a[i]);
        }

        int ans = -1;
        for (int i = L; i <= H; i++)
        {
            bool ok = true;
            rep(j, N)
            {
                if (i < a[j] && a[j] % i == 0)
                    continue;
                if (i >= a[j] && i % a[j] == 0)
                    continue;
                ok = false;
                break;
            }
            if (ok)
            {
                ans = i;
                break;
            }
        }
        if (ans == -1)
            puts("NO");
        else
            printf("%d\n", ans);
    }

    return 0;
}
