#include<stdio.h>

int main()
{
    int i, j, k;
    int nowt, t;
    int sum, minvalue, sumxor;
    int n, a;

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    scanf("%d", &t);
    nowt = 0;
    while (t --) {
        nowt ++;
        scanf("%d", &n);
        sum = sumxor = 0;
        minvalue = -1;
        for (i = 0; i < n; i ++) {
            scanf("%d", &a);
            sum += a;
            sumxor ^= a;
            if (minvalue < 0)
                minvalue = a;
            else if (minvalue > a)
                minvalue = a;
        }

        if (sumxor != 0)
            printf("Case #%d: NO\n", nowt);
        else
            printf("Case #%d: %d\n", nowt, sum - minvalue);
    }
    return 0;
}

