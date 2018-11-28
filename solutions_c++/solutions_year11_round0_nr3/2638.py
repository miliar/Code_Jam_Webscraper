#include<iostream>
#include<cstdio>

using namespace std;

int n;
int sum, bsum, mn;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        sum = bsum = 0;
        mn = 999999999;
        scanf("%d", &n);
        for(int i = 0; i < n; ++i)
        {
            int a;
            scanf("%d", &a);
            bsum ^= a;
            sum += a;
            mn = min(mn, a);
        }
        printf("Case #%d: ", Ti);
        if(bsum)
            puts("NO");
        else
            printf("%d\n", sum - mn);
    }
    return 0;
}
