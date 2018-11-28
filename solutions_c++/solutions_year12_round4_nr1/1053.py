#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 10010;

int n, d;
int nxt[N];
int p[N], l[N];
bool res;

int main()
{
    
    freopen("alarge.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d %d", p + i, l + i);
        scanf("%d", &d);
        fill(nxt, nxt + n, -1);
        res = false;

        nxt[0] = p[0];
        for (int i = 0; i < n; i++)
            if (nxt[i] != -1)
                for (int j = i + 1; j < n; j++)
                    if (p[j] <= p[i] + nxt[i])
                        nxt[j] = max(min(p[j] - p[i], l[j]), nxt[j]);
                    else
                        break;
        for (int i = n - 1; i >= 0 && !res; i--)
            if (nxt[i] != -1 && d <= nxt[i] + p[i])
                res = true;
        if (res)
            printf("Case #%d: YES\n", cas);
        else
            printf("Case #%d: NO\n", cas);
    }
    return 0;
} 