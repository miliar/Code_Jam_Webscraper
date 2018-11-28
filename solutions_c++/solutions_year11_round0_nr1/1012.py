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

const int size = 1000 * 10;
char buf[size];

int main()
{
    int t, mv, ps[2], tc, ltm[2], p, tp, n, i;
    char c1, c2;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (t = 0; t < tc; t++)
    {
        cin >> n;
        ps[0] = 1;
        ps[1] = 1;
        ltm[0] = 0;
        ltm[1] = 0;
        mv = 0;
        for (i = 0; i < n; i++)
        {
            cin >> c1 >> p;
            //cerr << c1 << ' ' << c2 << ' ' << p << endl;
            tp = (c1 == 'O');
            mv += max(0, - (mv - ltm[tp]) + (abs(p - ps[tp])));
            ps[tp] = p;
            mv++;
            ltm[tp] = mv;
        }
        cout << "Case #" << t + 1 << ": " << mv << endl;
    }

    return 0;
}
