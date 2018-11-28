#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    //freopen("b.in", "r", stdin);
    //freopen("b.out", "w", stdout);

    int t; cin >>t;
    for (int tt = 1; tt <= t; ++ tt)
    {
        int l, p, c; cin >>l >>p >>c;
        int ans = 0;
        double tot = c, compare = 1.0 * p / l;
        while (tot < compare)
        {
            ans ++;
            tot *= tot;
        }
        cout <<"Case #" <<tt <<": " <<ans <<endl;
    }
    return 0;
}
