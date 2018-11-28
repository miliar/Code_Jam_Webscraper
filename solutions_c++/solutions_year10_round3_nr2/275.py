#include <stdio.h>

#include <math.h>

double logbase(int b,double x) {

   return (log(x))/(log(b));

}

main() {

    int T,t;
    int L,P,C;
    double tests = 0.0;
    double l1,l2;
    int i1,i2;
    scanf("%d",&T);

    for (t = 1; t <=T; t++) {

      scanf("%d %d %d",&L,&P,&C);

      tests = 0.0;
      if (P > C*L) {
         l1 = ceil(logbase(C,((double)P)/L) );


         tests = ceil(logbase(2,l1));
      }

      printf("Case #%d: %.0f\n",t,tests);
    }
}
