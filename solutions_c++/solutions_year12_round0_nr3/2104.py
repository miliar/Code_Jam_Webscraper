#include <iostream>
#include <cstdio> ;
using namespace std ;
void error(const char *s) {
   fprintf(stderr, "%s\n", s) ;
   exit(10) ;
}
int incr(int v) {
   v++ ;
   int d = 0 ;
   while (((v >> (4 * d)) & 15) >= 10) {
      v += 6 << (4 * d) ;
      d++ ;
   }
   return v ;
}
int main(int argc, char *argv[]) {
   int kases = 0 ;
   if (scanf("%d\n", &kases) != 1)
      error("! parse error") ;
   for (int kase=1; kase<=kases; kase++) {
      int A=0, B=0 ;
      if (scanf("%x %x\n", &A, &B) != 2)
         error("! parsing args") ;
      int digs = 0 ;
      while (A >> (4 * digs))
         digs++ ;
      int r = 0 ;
      for (int i=A; i<B; i=incr(i)) {
         int t = i ;
         while (1) {
            t = (t >> 4) + ((t & 15) << (4 * (digs - 1))) ;
            if (t == i)
               break ;
            if (t > i && t <= B)
               r++ ;
         }
      }
      printf("Case #%d: %d\n", kase, r) ;
   }
}
