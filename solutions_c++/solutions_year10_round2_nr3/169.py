




/*
  Program   :   Your Rank is Pure
  Author    :   czshs_yk
  Date      :   23/05/10
  Source    :   Google Code Jam 2010 Round 1
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int maxn = 500 + 5;
const int inf  = 100003;

int T, n, res;
int c[maxn][maxn], s[maxn][maxn];

int main () {
    freopen ("C.in" , "r", stdin );
    freopen ("C.out", "w", stdout);
    
    memset (c, 0, sizeof (c));
    memset (s, 0, sizeof (s));
    for (int i = 0; i <= maxn; ++ i) {
        c[i][0] = 1;
        for (int j = 1; j <= i; ++ j)
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % inf;
    }
    s[1][0] = 1;
    for (int i = 2; i <= maxn; ++ i)
        for (int j = 1; j < i; ++ j) 
            for (int k = 0; k < j; ++ k) {
                long long temp = s[j][k];
                temp *= c[i - j - 1][j - k - 1];
                temp %= inf;
                s[i][j] = (s[i][j] + temp) % inf;
            }
            
    scanf ("%d", &T);
    for (int i = 1; i <= T; ++ i) {
        scanf ("%d", &n);
        res = 0;
        for (int j = 1; j < n; ++ j)
            res = (res + s[n][j]) % inf;
        printf ("Case #%d: %d\n", i, res);
    }
    
    return 0;
}
