#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <ctime>
using namespace std;


#define forn(i, n) for(int i = 0; i < n; i++)

int n, curr_d, d[10002], l[10002], D, m, r[10002], max_l;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for(int test = 1; test <= n; test++)
    {
        curr_d = 0;
        cin >> m;
        cin >> d[0] >> l[0];
        l[0] = d[0];
        r[0] = 1;
        for(int i = 1; i < m; i++)
        {
            r[i] = 0;
            cin >> d[i] >> max_l;
            for(int j = i - 1; j >= 0; j--)
                if(d[j] + l[j] >= d[i]  &&  r[j])
                {
                    l[i] = min(d[i] - d[j], max_l);
                    r[i] = true;
                }

        }
        cin >> d[m];
        r[m + 1] = 0;
        for(int i = 0; i < m; i++)
            if(d[i] + l[i] >= d[m]  &&  r[i])
            {
                r[m + 1] = true;
            }

        printf("Case #%d: ", test);
        if(r[m + 1])
            printf("YES\n");
        else
            printf("NO\n");
    }
}
