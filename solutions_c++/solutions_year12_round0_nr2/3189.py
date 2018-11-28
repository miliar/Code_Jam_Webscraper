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

int t, n, s, p, k, ans;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int test = 1; test <= t; test++)
    {
        cin >> n >> s >> p;
        ans = 0;
        forn(i, n)
        {
            cin >> k;
            if(k >= 3 * p - 2  &&  k >= p)  ans++;
            else
                if(k >= 3 * p - 4  &&  s > 0  &&  k >= p)
                {
                    ans++;
                    s--;
                }
        }
        printf("Case #%d: %d\n", test, ans);
    }
}
