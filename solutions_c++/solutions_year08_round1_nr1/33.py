#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int t;
int n;
int x[10000];
int y[10000];

int main()
{
    scanf("%d", &t);

    for (int index = 1; index <= t; ++index)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d", &x[i]);
        for (int i = 0; i < n; ++i)
            scanf("%d", &y[i]);

        sort(x, x + n);
        sort(y, y + n);
        reverse(y, y + n);

        long long sum = 0;
        long long tmp;
        for (int i = 0; i < n; ++i)
        {
            tmp = x[i];
            tmp *= y[i];
            sum += tmp;
        }

        cout << "Case #" << index << ": " << sum << endl;
    }

    return 0;
}
