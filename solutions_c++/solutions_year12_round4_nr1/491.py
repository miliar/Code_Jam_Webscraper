#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <math.h>

#define Pi acos(-1.0)
#define INT_MAX 2147000000
#define mp make_pair
#define pb push_back

#define EPS 1e-13

using namespace std;

int t, D;
int a[100000], b[100000], d[100000], l[100000];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int tc = 1; tc <= t; tc++)
    {
        int n;
        cin >> n;
        memset(a, 0, n * 4);
        memset(b, 0, n * 4);

        for (int i = 0; i < n; i++)
            cin >> d[i] >> l[i];
        cin >> D;
        a[0] = 1;
        b[0] = d[0];

        int maxx = d[0];
        for (int i = 0; i < n; i++)
        {
            if (a[i])
            {
                int x = d[i] + b[i];
                if (x >= maxx)
                {
                    maxx = x;
                }
                for (int j = i + 1; j < n && d[j] <= x; j++)
                {
                    a[j] = 1;
                    int t = min(l[j],d[j]-d[i]);
                    if (t > b[j]) b[j] = t;
                }
            }
        }


        cout << "Case #" << tc << ": ";
        if (maxx >= D)
            cout << "YES\n";
        else
            cout << "NO\n";
    }


    return 0;
}
