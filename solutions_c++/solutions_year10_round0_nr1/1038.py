#include <iostream>
#include <cstdio>
using namespace std;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, t;
    cin >> T;

    for (t = 1; t <= T; t ++)
    {
        printf("Case #%d: ", t);

        int n, k;
        cin >> n >> k;

        bool ok = 1;
        for (int i = 0; i < n; i ++)
        {
            if (k % 2 == 0) ok = 0;
            k /= 2;
        }

        if (ok) puts("ON");
        else puts("OFF");
    }
}