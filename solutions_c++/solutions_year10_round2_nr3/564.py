#include <iostream>

int t;
int n;
int main()
{
    freopen("3.in", "r", stdin);
    freopen("3.out", "w", stdout);
    int ans[] = {0, 0, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 40265, 68060, 13335, 84884};
    scanf("%d", &t);
    for(int i= 1; i <= t; i++)
    {
        scanf("%d", &n);
        printf("Case #%d: %d\n", i, ans[n]);
    }
    return 0;
}
