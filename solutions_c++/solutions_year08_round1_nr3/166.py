#include <iostream>
#include <cmath>
using namespace std;
int t, n;
const int a[40] = {0, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};

int main () {
    freopen("c.out", "w", stdout);
    scanf ("%d", &t);
    int c = 1;
    while (t--) {
        scanf ("%d", &n);
        printf ("Case #%d: %03d\n", c++, a[n]);
    }
    return 0;
}
