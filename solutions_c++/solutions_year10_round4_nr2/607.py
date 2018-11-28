




/*
  Program   :   World Cup 2010
  Author    :   czshs_yk
  Date      :   05/06/10
  Source    :   Google Code Jam 2010 Round 2
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int T, p;
int c[11][1100], s[20][1100][20], m[1100];

int main () {
    freopen ("B.in" , "r", stdin );
    freopen ("B.out", "w", stdout);
    
    scanf ("%d", &T);
    for (int r = 1; r <= T; ++ r) {
        scanf ("%d", &p);
        for (int i = 1; i <= (1 << p); ++ i)
            scanf ("%d", &m[i]);
        for (int i = 1; i <= p; ++ i)
            for (int j = 1; j <= (1 << (p - i)); ++ j)
                scanf ("%d", &c[i][j]);
                
        memset (s, 7, sizeof (s));
        for (int i = 1; i <= (1 << p); ++ i)
            s[0][i][p - m[i]] = 0;
        for (int i = 1; i <= (1 << p); ++ i)
            for (int j = 1; j <= p; ++ j)
                s[0][i][j] = min (s[0][i][j], s[0][i][j - 1]);
        for (int i = 1; i <= p; ++ i)
            for (int j = 1; j <= (1 << (p - i)); ++ j)
                for (int k = 0; k <= p - i; ++ k) {
                    s[i][j][k] <?= s[i - 1][j * 2 - 1][k] + s[i - 1][j * 2][k];
                    if (s[i - 1][j * 2 - 1][k + 1] + s[i - 1][j * 2][k + 1]
                      + c[i][j] < s[i][j][k])
                    s[i][j][k] = s[i - 1][j * 2 - 1][k + 1] 
                               + s[i - 1][j * 2][k + 1] + c[i][j]; 
                }
        printf ("Case #%d: %d\n", r, s[p][1][0]);
    }
    
    return 0;
}
