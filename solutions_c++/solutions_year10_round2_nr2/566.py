#include <cstdio>

using namespace std;

static inline bool canmakeit(int x, int v, int b, int t, int i) {
   return x + v*t >= b;
}

int main() {
   int c;
   scanf("%d", &c);
   for (int ci = 1; ci <= c; ci++) {
      int n, k, b, t;
      scanf("%d %d %d %d", &n, &k, &b, &t);
      int x[n], v[n];
      int ops = 0, madeit = 0;
      for (int ni = 0; ni < n; ni++) {
         scanf("%d", &x[ni]);
      }
      for (int ni = 0; ni < n; ni++)
         scanf("%d", &v[ni]);
      for (int i = n-1; i >= 0; i--) {
         if (madeit == k)
            break;
         if (canmakeit(x[i], v[i], b, t, i)) {
            madeit++;
            for (int j = i+1; j < n; j++)
               if (!canmakeit(x[j], v[j], b, t, i))
                  ops++;
         }
      }
      printf("Case #%d: ", ci);
      if (madeit == k)
         printf("%d\n", ops);
      else
         printf("IMPOSSIBLE\n");
   }
   return 0;
}
