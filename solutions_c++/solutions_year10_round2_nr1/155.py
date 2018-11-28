




/*
  Program   :   File Fix-it
  Author    :   czshs_yk
  Date      :   23/05/10
  Source    :   Google Code Jam 2010 Round 1
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int maxn = 200 + 5;
const int maxl = 100 + 5;

int T, n, m, res;
char temp;
char c[maxn][maxl][maxl];
int s[maxn], len[maxn][maxl];

bool check (int x, int y, int z) {
     if (z > s[x] || z > s[y]) return false;
     if (len[x][z] != len[y][z]) return false;
     for (int k = 1; k <= len[x][z]; ++ k)
         if (c[x][z][k] != c[y][z][k]) return false;
     return true;
}

int main () {
    freopen ("A.in" , "r", stdin );
    freopen ("A.out", "w", stdout);
    
    scanf ("%d", &T);
    for (int i = 1; i <= T; ++ i) {
        res = 0; int k = 0;
        memset (s, 0, sizeof (s));
        memset (len, 0, sizeof (len));
        scanf ("%d %d", &n, &m);
        temp = getchar (); 
        for (int j = 1; j <= n + m; ++ j) {
            temp = getchar ();
            while (isalpha (temp) || isdigit (temp) || temp == '/') {
                  if (temp != '/') 
                     c[j][s[j]][++ k] = temp;
                  else {
                     len[j][s[j]] = k;  
                     ++ s[j]; k = 0;  
                  }
                  temp = getchar ();
            }
            len[j][s[j]] = k;
            k = 0;
        }
        
        for (int j = n + 1; j <= n + m; ++ j) {
            int maxs = 0;
            for (int v = 1; v < j; ++ v) {
                int cc = 1;
                while (check (v, j, cc)) ++ cc;
                maxs = max (maxs, cc - 1);
            }
            res += (s[j] - maxs);
        }
        printf ("Case #%d: %d\n", i, res);
    }
    
    return 0;
}
