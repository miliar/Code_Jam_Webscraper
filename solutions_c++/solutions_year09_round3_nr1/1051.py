#include <iostream>
#include <cstring>
using namespace std;

#define LL long long
#define N 100

LL ans;
char s[N];
int a[N];
bool used[N];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-samll.out", "w", stdout);
    int t, cas;
    scanf("%d", &cas);
    for (t = 1; t <= cas; ++t)
    {
        int i, j, k, n;
        scanf("%s", s);
        n = strlen(s);
        memset(used, 0, sizeof(used));
        a[0] = 1;
        used[1] = 1;
        for (i = 1; i < n; ++i)
        {
            k = -1;
            for (j = 0; j < i; ++j)
                if (s[i] == s[j])
                {
                    k = a[j];
                    break;
                }
            if (k == -1)
            {
                for (k = 0; k < N; ++k)
                    if (!used[k])
                        break;
            }
            a[i] = k;
            used[k] = 1;
        }
        int max = 0;
        for (i = 0; i < n; ++i)
            if (a[i] > max)
               max = a[i];
        ++max;
        ans = 0;
        for (i = 0; i < n; ++i)
            ans = ans * max + a[i];
        printf("Case #%d: %lld\n", t, ans);
    }
    return 0;
}
