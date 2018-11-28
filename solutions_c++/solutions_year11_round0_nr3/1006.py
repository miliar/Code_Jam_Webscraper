#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define PI 3.1415926535897932384626433832795

const int inf = 1000 * 1000 * 1000;

int main()
{
    int i, t, tc, mn, xr, sum, v, n;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (t = 0; t < tc; t++)
    {
        cin >> n;
        xr = 0;
        sum = 0;
        mn = inf;
        for (i = 0; i < n; i++)
        {
            cin >> v;
            xr ^= v;
            sum += v;
            mn = min(mn, v);
        }
        if (xr)
            cout << "Case #" << t + 1 << ": NO" << endl;
        else
            cout << "Case #" << t + 1 << ": " << sum - mn << endl;
    }

    return 0;
}
