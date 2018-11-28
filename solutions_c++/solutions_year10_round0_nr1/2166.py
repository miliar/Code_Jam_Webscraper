#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T, n, k, tot, ans;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", t);
        tot = (1 << n) - 1;
        if ((k % (tot+1)) == tot)
            puts("ON");
        else
            puts("OFF");
    }
    return 0;
}
