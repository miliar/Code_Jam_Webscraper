/**********************************************************************
Author: cominde
Created Time: Saturday, July 26, 2008 AM10:17:13 CST
File Name: files/code/codejam2/c/c3.cpp
**********************************************************************/
#include <iostream>
#include <cmath>

using namespace std;

int t, n;
const int a[40] = {0, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 463, 991,
                    95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};

int main () {
    freopen("c.out", "w", stdout);
    scanf ("%d", &t);
    int c = 1;
    while (t--) {
        scanf ("%d", &n);
//        long double ans = pow (3 + sqrt(5.0), n);
//        printf ("%lf\n", ans);
//        cout << ans << endl;
//        ans = ans - (double)((int)ans / 1000 * 1000);
        printf ("Case #%d: %03d\n", c++, a[n]);
    }
    return 0;
}
