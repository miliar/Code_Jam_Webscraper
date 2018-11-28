#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#define nabs(x) (x)<0?(-(x)):(x)
using namespace std;

int main()
{
    int t, k;
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> t;
    for(k = 1; k <= t; ++k)
    {
        printf("Case #%d: ", k);
        int n, l, h;
        int x[10005];
        int i, j;
        cin >> n >> l >> h;
        for(i = 0; i < n; ++i)
        {
            cin >> x[i];
        }
        for(i = l; i <= h; ++i)
        {
            for(j = 0; j < n; ++j)
            {
                if(i < x[j])
                {
                    if(x[j] % i != 0)
                        break;
                }
                else
                {
                    if(i % x[j] != 0)
                        break;
                }
            }
            if(j == n)
                break;
        }
        if(i <= h)
            printf("%d\n", i);
        else
            cout << "NO" << endl;
    }
    return 0;
}
