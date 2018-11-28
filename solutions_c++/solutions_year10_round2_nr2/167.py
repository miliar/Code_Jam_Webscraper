




/*
  Program   :   Picking Up Chicks
  Author    :   czshs_yk
  Date      :   23/05/10
  Source    :   Google Code Jam 2010 Round 1
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int maxn = 100 + 5;

int c, s, B, T, n, k, r;
int x[maxn], v[maxn], t[maxn];

int main () {
    freopen ("B.in" , "r", stdin );
    freopen ("B.out", "w", stdout);
    
    scanf ("%d", &c);
    for (int i = 1; i <= c; ++ i) {
        scanf ("%d %d %d %d", &n, &k, &B, &T);
        for (int j = 1; j <= n; ++ j)
            scanf ("%d", &x[j]);
        for (int j = 1; j <= n; ++ j)
            scanf ("%d", &v[j]);
        for (int p = 1; p < n; ++ p)
            for (int q = p + 1; q <= n; ++ q)
                if (x[p] < x[q]) {
                   swap (x[p], x[q]); swap (v[p], v[q]);
                }
        
        s = 0; r = 0;
        memset (t, 0, sizeof (t));
        for (int j = 1; j <= n; ++ j)
            if (x[j] + T * v[j] >= B) {
               -- k; t[j] = t[r] + (j - r - 1);
               s += t[j]; r = j;
               if (k == 0) break;
            }
        if (k > 0) 
           printf ("Case #%d: IMPOSSIBLE\n", i);
        else
           printf ("Case #%d: %d\n", i, s);
    }
    
    return 0;
}
