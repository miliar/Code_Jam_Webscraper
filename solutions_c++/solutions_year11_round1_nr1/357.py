#include<iostream>
using namespace std;
int gcd(int a, int b)
{
    if (a < b) return gcd(b, a);
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main()
{
    //freopen("AL.txt", "r", stdin);
    freopen("ALarge.out", "w", stdout);
    int t;scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++)
    {
        int pd, pg;
        long long n;
        scanf("%lld%d%d", &n, &pd, &pg);
        int d, g;
        bool flag = false;
        int t = gcd(pd, 100);
        long long tmp = 100 / t;
        if (tmp > n)
        {
            flag = false;
        }else
        {
            int d = 100 / t;
            int dwin = d * pd / 100;
            int dlose = d - dwin;
            if (pg != 0 && pg != 100 || (pg == 0 && dwin == 0) || (pg == 100 && dlose == 0))
            {
                flag = true;
            }
        }
        printf("Case #%d: ", tt);
        if (flag) printf("Possible\n");
        else printf("Broken\n");
    }
    return 0;
}
