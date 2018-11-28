#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

const int maxn = 2000;

char s[maxn], ss[maxn];
int casen, n, m;
int a[maxn], b[maxn];
bool f[maxn];
int ans;

void init()
{
     scanf("%d", &n);
     scanf("%s", &s);
     m = strlen(s);
}

void check(int i)
{
     if (i == n) {
        int base = 0;
        for (int i(0); i < m; ++i)
        {
            if (i % n == 0) base = i;
            ss[base + a[i % n]] = s[i];
        }
        //printf("%s\n", ss);  system("pause");
        int temp = 1;
        for (int i(1); i < m; ++i) if (ss[i] != ss[i - 1]) ++temp;
        ans = min(ans, temp);
        return;
     }
     for (int j(0); j < n; ++j) if (!f[j]) {
         f[j] = true;
         a[i] = j;
         check(i + 1);
         f[j] = false;
     }
}

void work()
{
     memset(f, 0, sizeof(f));
     ans = maxn;
     check(0);
     printf("%d\n", ans);
}
     

int main()
{
    freopen("D-small.txt", "r", stdin);
    freopen("D.out","w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        init();
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
