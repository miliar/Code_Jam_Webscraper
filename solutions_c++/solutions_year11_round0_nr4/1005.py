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

int main()
{
    int tc, t, n, i, cnt, v;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (t = 0; t < tc; t++)
    {
        cin >> n;
        cnt = 0;
        for (i = 0; i < n; i++)
        {
            cin >> v;
            cnt += (v == (i + 1));
        }
        cout << "Case #" << t + 1 << ": " << n - cnt << endl;
    }

    return 0;
}
