#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int t, n;
    int tx, ty, adx, ady;
    int i;
    int ad;
    char ch[4];

    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);

    scanf("%d", &t);
    for (i=1; i<=t; i++)
    {
        scanf("%d", &n);
        tx = ty = 0;
        adx = ady = 1;
        while (n--)
        {
            scanf("%s%d", ch, &ad);
            if (ch[0] == 'B')
            {
                tx = max(tx + abs(ad - adx), ty) + 1;
                adx = ad;
            }
            else
            {
                ty = max(ty + abs(ad - ady), tx) + 1;
                ady = ad;
            }
            //printf("!!! %d %d  %d %d\n", tx, ty, adx, ady);
        }
        printf("Case #%d: %d\n", i, max(tx, ty));
    }

    return 0;
}
