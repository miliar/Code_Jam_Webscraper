// vim:set ts=8 sw=4 et smarttab:
// Qualification Round 2011

#include <cstdio>
#include <cassert>

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        int n;
        scanf("%d", &n);
        int answer = 0;
        for (int i = 1; i <= n; ++i)
        {
            int temp;
            scanf("%d", &temp);
            if (temp != i)
                ++answer;
        }
        printf("Case #%d: %d\n", tc, answer);
    }
}
