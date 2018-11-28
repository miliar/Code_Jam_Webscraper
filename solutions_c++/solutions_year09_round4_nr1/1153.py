#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxn = 40 + 10;
const int inf = (-1u) >> 1;

int g[maxn][maxn];
char s[maxn][maxn], n, Case = 1;

void init()
{
    scanf ("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf ("%s", s[i]);
    
    memset (g, 0, sizeof(g));
    for (int i = 0, j; i < n; ++i) {
        //printf ("--%s\n", s[i]);
        for (j = n - 1; j >= 0; --j) {
            if (s[i][j] == '1')
                break;
        }
        if (j == -1)
            ++j;
        for (int k = j; k < n; ++k) 
            g[i][k] = 1;
    }
}

void solve()
{
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int j = i;
        while (!g[j][i])
            ++j;
        for (int k = j; k > i; --k) {
            ++ans;
            for (int s = 0; s < n; ++s)
                g[k][s] = g[k - 1][s];
        }
    }
    
    printf ("Case #%d: %d\n", Case++, ans);
}

int main()
{
    int t;
    freopen ("A-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);
    
    scanf ("%d", &t);
    while (t--) {
        init();
        solve();
    }
    
    //while (1);
    
    return 0;
}
