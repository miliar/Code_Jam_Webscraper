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

vector <pair <long double, long double> > sec;

int main()
{
    int tcnt, tc, i, n;
    long double x, s, r, t, last, ans, bi, ei, wi;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout.precision(20);
    cin >> tcnt;
    for (tc = 0; tc < tcnt; tc++)
    {
        cin >> x >> s >> r >> t >> n;
        sec.clear();
        sec.pb(mp(0, 0));
        last = 0;
        for (i = 0; i < n; i++)
        {
            cin >> bi >> ei >> wi;
            sec.pb(mp(wi, ei - bi));
            sec[0].sc += bi - last;
            last = ei;
        }
        sec[0].sc += x - ei;
        sort(sec.begin(), sec.end());
        ans = 0;
        for (i = 0; i < sec.size(); i++)
        {
            if (t > 0)
            {
                if (sec[i].sc > (sec[i].fs + r) * t)
                {
                    sec[i].sc -= (sec[i].fs + r) * t;
                    ans += t;
                    t = 0;
                    ans += (sec[i].sc / (sec[i].fs + s));
                    sec[i].sc = 0;
                }
                else
                {
                    ans += sec[i].sc / (sec[i].fs + r);
                    t -= sec[i].sc / (sec[i].fs + r);
                    sec[i].sc = 0;
                }
            }
            else
            {
                ans += (sec[i].sc / (sec[i].fs + s));
                sec[i].sc = 0;
            }
        }
        cout << "Case #" << tc + 1 << ": " << ans << endl;
    }

    return 0;
}
