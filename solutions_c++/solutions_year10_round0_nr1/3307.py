#include <cstdio>

int main()
{
    int result[30] = {1};
    for (int i = 1; i < 30; ++i)
           result[i] = 2*result[i - 1] + 1;

    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int p = 1; p <= t; ++p)
    {
       int n, k;
       scanf("%d%d", &n, &k);
       printf("Case #%d: ", p);

       if (result[n - 1] == k) printf("ON\n");
       else if (k % (result[n - 1] + 1) == result[n - 1]) printf("ON\n");
       else printf("OFF\n");

    }
}
