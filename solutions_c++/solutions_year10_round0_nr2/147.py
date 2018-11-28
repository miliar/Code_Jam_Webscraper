#include <iostream>

using namespace std;

int ab(int a) {return (a > 0 ? a : -a);}
int gcd(int a, int b) {return (b ? gcd(b, a % b) : a);}

void solve(int test)
{
    int n;
    int t[10], g[10];
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++)
        scanf("%d", &t[i]);
    for (int i = 2; i <= n; i ++)
        g[i] = ab(t[i] - t[1]);

    int d = g[2];
    for (int i = 2; i <= n; i ++)
        d = gcd(d, g[i]);
    int p = t[1] % d;
    if (p != 0) p = d - p;
    printf("Case #%d: %d\n", test, p);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    scanf("%d", &test);
    for (int i = 1; i <= test; i ++)
        solve(i);
    return 0;
}