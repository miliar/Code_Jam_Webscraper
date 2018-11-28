#include<cstdio>
#include <cstring>

using namespace std;

const int MAXN = 100;

int T, N, p, c1, c2;
int p1[MAXN], p2[MAXN], t1, t2, t3;
int p3[MAXN];
char ch;

int abs (int x) { return x > 0 ? x : -x; }
int MIN (int a, int b) { return a < b ? a : b; }

int main ()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("ou.txt", "w", stdout);
    
    scanf ("%d", &T);
    for (int i = 1; i <= T; i++) {
      scanf ("%d", &N);
      
      t1 = t2 = t3 = 0;
      c1 = c2 = 1;
      for (int j = 0; j < N; j++) {
        ch = getchar ();
        while (ch != 'O' && ch != 'B') ch = getchar ();
        
        scanf ("%d", &p);
        
        if (ch == 'O') p1[t1 ++] = p, p3[j] = 0; else p2[t2 ++] = p, p3[j] = 1; 
      }
      
      int i1 = 0, i2 = 0, ans = 0;
      for (int j = 0; j < N; j++) {
        int min = 1000;
        if (i1 < t1) min = MIN (min, abs (p1[i1] - c1));
        if (i2 < t2) min = MIN (min, abs (p2[i2] - c2));
        
        ans += min;
        
        int d1 = p1[i1] < c1 ? -1 : 1;
        int d2 = p2[i2] < c2 ? -1 : 1;

        c1 += d1 * min;
        c2 += d2 * min;
        
        if (p3[j] == 0) {
          ans += abs (p1[i1] - c1);
          c1 = p1[i1];
          i1 ++;
          
          if (i2 < t2 && c2 != p2[i2]) c2 += d2; 
        } else {
          ans += abs (p2[i2] - c2);
          c2 = p2[i2];
          i2 ++;
          if (i1 < t1 && c1 != p1[i1]) c1 += d1; 
        }
        
        ans ++;
        
        //printf ("%d %d %d\n", c1, c2, ans);
      }
      
      printf ("Case #%d: %d\n", i, ans);
    }
}
