#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int t, n, sum;
int minn, tot, num;

int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++)
    {
        scanf("%d", &n);
        minn = 1000000;
        sum = 0, tot = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &num);
            sum ^= num, tot += num;
            if (num < minn) minn = num;
        }
        printf("Case #%d: ", cas);
        if (sum == 0) printf("%d\n", tot - minn);
        else printf("NO\n");
    }
    return 0;
}
