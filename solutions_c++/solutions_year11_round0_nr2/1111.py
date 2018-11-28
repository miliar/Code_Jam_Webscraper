#include <iostream>
#include <cstring>

#define N 16
using namespace std;

int main()
{
    int t, test = 1, a, b, L, n;
    int i, j, k;
    char ca[64][4], cb[64][4], str[128], ans[128];

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--)
    {
        scanf("%d", &a);
        for (i=0; i<a; i++)
            scanf("%s", ca[i]);
        scanf("%d", &b);
        for (i=0; i<b; i++)
            scanf("%s", cb[i]);
        scanf("%d", &L);
        scanf("%s", str);
        n = 1;
        ans[0] = str[0];

        for (i=1; i<L; i++)
        {
            ans[n] = str[i];
            n++;
            while (n > 1)
            {
                for (j=0; j<a; j++)
                    if ((ans[n-1] == ca[j][0] && ans[n-2] == ca[j][1]) || (ans[n-1] == ca[j][1] && ans[n-2] == ca[j][0]))
                    {
                        ans[n-2] = ca[j][2];
                        n--;
                        break;
                    }
                if (j < a)
                    continue;

                for (j=0; j<b; j++)
                    if (ans[n-1] == cb[j][0])
                    {
                        for (k=n-2; k>=0 && ans[k]!=cb[j][1]; k--);
                        if (k >= 0)
                        {
                            n = 0;
                            break;
                        }
                    }
                if (j < b)
                    continue;

                for (j=0; j<b; j++)
                    if (ans[n-1] == cb[j][1])
                    {
                        for (k=n-2; k>=0 && ans[k]!=cb[j][0]; k--);
                        if (k >= 0)
                        {
                            n = 0;
                            break;
                        }
                    }
                if (j == b)
                    break;
            }
        }

        printf("Case #%d: [", test++);
        for (i=0; i<n-1; i++)
            printf("%c, ", ans[i]);
        if (n)
            printf("%c", ans[n-1]);
        printf("]\n");
    }

    return 0;
}
