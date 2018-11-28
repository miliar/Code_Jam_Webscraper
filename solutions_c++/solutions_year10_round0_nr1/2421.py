#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    const int maxn = 40;
    long long check[40] = {0};
    check[0] = 2;
    for (int i = 1; i < 40; ++ i)
        check[i] = check[i - 1] * 2;
    long long t; cin >>t;
    for (int i = 0; i < t; ++ i)
    {
        long n, k; cin >>n >>k;
        cout <<"Case #" << i + 1 <<": " <<(((k +1)%check[n-1])?"OFF":"ON") <<endl;
    }
}
