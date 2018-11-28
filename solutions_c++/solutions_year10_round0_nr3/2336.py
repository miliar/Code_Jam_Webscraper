#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    const int maxn = 1000;
    long num[maxn] = {0};
    long long ans = 0;
    int r, k, n;

    int t; cin >>t;
    for (int t1 = 0; t1 < t; ++ t1)
    {
        ans = 0;
        cin >>r >>k >>n;
        for (int i = 0; i < n; ++ i) cin >>num[i];
        int index = 0, head = 0;
        for (int i = 0; i < r; ++ i)
        {
            int tot = num[index];
            while (((index + 1) % n != head) && (tot + num[(index + 1) % n] <= k)) tot +=num[(++index) % n];
            ans += tot;
            head = index = (index + 1) % n;
        }
        cout <<"Case #" <<t1 + 1 <<": " <<ans <<endl;
    }
}
