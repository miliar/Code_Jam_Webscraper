#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;

int T, c, d, n, top;
char g[300][300];
char cmd[110], stack[110];
bool forb[300][300];

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    char ss[5];
    scanf("%d", &T);
    for (int cases = 1; cases <= T; ++cases)
    {
        top = 0;
        scanf("%d", &c);
        memset(g, 0, sizeof (g));
        memset(forb, 0, sizeof (forb));
        memset(stack, 0, sizeof (stack));
        for (int i = 1; i <= c; ++i)
        {
            scanf("%s", ss);
            g[ss[0]][ss[1]] = ss[2];
            g[ss[1]][ss[0]] = ss[2];
        }
        scanf("%d", &d);
        for (int i = 1; i <= d; ++i)
        {
            scanf("%s", ss);
            forb[ss[0]][ss[1]] = 1;
            forb[ss[1]][ss[0]] = 1;
        }
        scanf("%d%s", &n, cmd + 1);

        for (int i = 1; i <= n; ++i)
        {
            stack[++top] = cmd[i];
            if (top >= 2)
            {
                if (g[stack[top]][stack[top - 1]])
                {
                    stack[top - 1] = g[stack[top]][stack[top - 1]];
                    top--;
                }
            }
            for (int j = top - 1; j >= 1; --j)
            {
                if (forb[stack[j]][stack[top]])
                {
                    top = 0;
                    break;
                }
            }
        }
        printf("Case #%d: [", cases);
        if (top) printf("%c", stack[1]);
        for (int i = 2; i <= top; ++i)
            printf(", %c", stack[i]);
        puts("]");
    }
    return 0;
}