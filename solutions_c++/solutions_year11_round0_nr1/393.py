#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <math.h>

void init(void)
{
    int cas;
    scanf("%d", &cas);
    for (int k = 1; k <= cas; ++k)
    {
        int n, t = 0, lt[2] = {0, 0}, pos[2] = {1, 1};
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            char str[3];
            int but;

            scanf("%s%d", str, &but);
            int cur = (str[0] - 'A') % 2;
            int cost = abs(but - pos[cur]);

            pos[cur] = but;
            if (lt[cur] == 0)
            {
                t += cost + 1;
                lt[1 ^ cur] += cost + 1;
            }
            else
            {
                int tmp = (cost <= lt[cur]) ? 0 : (cost - lt[cur]);
                t += tmp + 1;
                lt[cur] = 0;
                lt[1 ^ cur] = tmp + 1;
            }
        }
        printf("Case #%d: %d\n", k, t);
    }
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    init();
    fclose(stdin);
    fclose(stdout);
    return 0;
}
