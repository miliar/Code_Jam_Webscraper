#include <iostream>
#include <cstdio> ;
using namespace std ;
void error(const char *s) {
   fprintf(stderr, "%s\n", s) ;
   exit(10) ;
}
int main(int argc, char *argv[]) {
   int kases = 0 ;
   if (scanf("%d\n", &kases) != 1)
      error("! parse error") ;
   for (int kase=1; kase<=kases; kase++) {
      int N = 0 ;
      int S = 0 ;
      int p = 0 ;
      if (scanf("%d %d %d", &N, &S, &p) != 3)
         error("! parse error") ;
      int r = 0 ;
      for (int i=0; i<N; i++) {
         int v = 0 ;
         if (scanf("%d", &v) != 1)
            error("! parse error") ;
         int b = 0 ;
         if (v < 2) { // cannot be surprising
            b = (v + 2) / 3 ;
         } else if (v > 28) { // cannot be surprising
            b = (v + 2) / 3 ;
         } else {
            int nsb = (v + 2) / 3 ;
            int sb = (v + 4) / 3 ;
            if (sb >= p && nsb < p && S > 0) {
               b = sb ;
               S-- ;
            } else
               b = nsb ;
         }
         if (b >= p)
            r++ ;
      }
      printf("Case #%d: %d\n", kase, r) ;
   }
}
