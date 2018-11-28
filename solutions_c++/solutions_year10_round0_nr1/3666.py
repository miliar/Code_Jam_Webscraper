




/*
  Program   :   Snapper Chain
  Author    :   czshs_yk
  Date      :   08/05/10
  Source    :   Gcj 2010 Qualification Round
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int T, n, k;

int main () {
    freopen ("A.in" , "r", stdin );
    freopen ("A.out", "w", stdout);
    
    scanf ("%d", &T);
    for (int i = 1; i <= T; ++ i) {
        scanf ("%d %d", &n, &k); ++ k;
        int c = k & -k, s = 1 << n;
        printf ("Case #%d: O%s\n", i, c >= s ? "N" : "FF");
    }
    
    return 0;
}
