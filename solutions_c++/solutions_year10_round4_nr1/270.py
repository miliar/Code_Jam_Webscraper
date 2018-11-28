




/*
  Program   :   Elegant Diamond
  Author    :   czshs_yk
  Date      :   05/06/10
  Source    :   Google Code Jam 2010 Round 2
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int maxn = 100;
const int inf  = 1 << 30;

int T, k, s;
char c[maxn][maxn];

bool check (int dx, int dy) {
     bool cc[10];
     
     for (int i = 1; i < 2 * k; ++ i)
         for (int j = 1; j < 2 * k; ++ j) {
             int xx = 2 * dx - i, yy = 2 * dy - j, zz = 0;
             memset (cc, 0, sizeof (cc));
             if (c[i][j] != ' ') ++ cc[c[i][j] - '0'];
             if (xx > 0 && xx < 2 * k && c[xx][j] != ' ')
                ++ cc[c[xx][j] - '0'];
             if (yy > 0 && yy < 2 * k && c[i][yy] != ' ')
                ++ cc[c[i][yy] - '0'];
             if (xx > 0 && xx < 2 * k && yy > 0 && yy < 2 * k)
                if (c[xx][yy] != ' ') ++ cc[c[xx][yy] - '0'];
             for (int r = 0; r <= 9; ++ r)
                 if (cc[r]) ++ zz;
             if (zz > 1) return false;
         }
     return true;
}

int dist (int dx, int dy) {
    int d = 0;
    for (int i = 1; i < 2 * k; ++ i)
        for (int j = 1; j < 2 * k; ++ j)
            if (c[i][j] != ' ') d = max (d, abs (i - dx) + abs (j - dy));
    return (d + 1) * (d + 1) - k * k;
}

int main () {
    freopen ("A.in" , "r", stdin );
    freopen ("A.out", "w", stdout);
    
    scanf ("%d", &T);
    for (int i = 1; i <= T; ++ i) {
        scanf ("%d", &k);
        for (int x = 0; x <= maxn; ++ x)
            for (int y = 0; y <= maxn; ++ y)
                c[x][y] = ' ';
        for (int x = 1; x <= k; ++ x) {
            char tmp = getchar ();
            for (int y = 1; y < k + x; ++ y)
                c[x][y] = getchar ();
        }
        for (int x = k + 1; x < 2 * k; ++ x) {
            char tmp = getchar ();
            for (int y = 1; y < 3 * k - x; ++ y)
                c[x][y] = getchar ();
        }
        
        s = inf;
        for (int x = 1; x < 2 * k; ++ x)
            for (int y = 1; y < 2 * k; ++ y)
                if (check (x, y))
                   s = min (s, dist (x, y));
        printf ("Case #%d: %d\n", i, s);
    }
    
    return 0;   
}
