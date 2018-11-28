#include <stdio.h>
#include <algorithm>

int T, n;
int aa[801], bb[801];

int main()
{
    int i, j, k;
    int nMin = 0;

	scanf("%d", &T);
    for (i = 1; i <= T; ++i)
    {
        scanf("%d", &n);
        for (j = 0; j < n; ++j)
            scanf("%d", &aa[j]);
        for (j = 0; j < n; ++j)
            scanf("%d", &bb[j]);

        std::sort(aa, aa + j);
        std::sort(bb, bb + j);

        nMin = 0;
        for (k = 0; k < j; ++k)
        {
            nMin += aa[j - k - 1] * bb[k];
        }
        printf("Case #%d: %d\n", i, nMin);
    }
    return 0;
}
