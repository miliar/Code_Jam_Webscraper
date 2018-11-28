#include<stdio.h>
#include<string>
#include<math.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>

using namespace std;

bool check(int n, int pd, int pg)
{
    int i, j, k;
    int a, b;

    if (pg == 0 && pd != 0)
        return false;

    if (pg == 100 && pd != 100)
        return false;

    a = pd;
    b = 100;
    for (i = 2; i <= a; i ++) {
        while (a % i == 0 && b % i == 0) {
            a /= i;
            b /= i;
        }
    }

    if (pd != 0 && b > n)
        return false;

    return true;
}

int main()
{
    int i, j, k;
    int t, nowt;
    int n, pd, pg;

    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    scanf("%d", &t);
    nowt = 0;
    while (t --) {
        nowt ++;
        scanf("%d%d%d", &n, &pd, &pg);
        if (check(n, pd, pg))
            printf("Case #%d: Possible\n", nowt);
        else
            printf("Case #%d: Broken\n", nowt);
    }

    return 0;
}