/*
Author: LotK
LANG: C++
*/

#include <cstdio>
#include <cstdlib>

double p[100003];
int main() {

    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);



    int t, tt, A, B, i, j;
    double ans, keepType , backOnce, backTwo, enRight;
    double mul, uu, ux, xu, xx;
    scanf("%d", &tt);
    for(t=0 ; t<tt ; t++) {
        scanf("%d%d", &A, &B);
        for(i=0 ; i<A ; i++) {
            scanf("%lf", &p[i]);
        }
        mul = 1;
        for(i=0 ; i<A-2 ; i++) {
            mul *= p[i];
        }

        ans = 0;
        keepType = 0;
        backOnce = 0;
        backTwo = 0;
        enRight = 0;

        if(A<2) {
            keepType = p[0]*(B-1+1);
            keepType += (1-p[0])*(B + B+1);
            backOnce = p[0]*(2 + B-1+1);
            backOnce += (1-p[0])*(2 + B);

            ans = keepType;
            if(ans > backOnce) ans = backOnce;
        }
        else {
            uu = mul*p[A-2]*p[A-1];
            ux = mul*p[A-2]*(1-p[A-1]);
            xu = mul*(1-p[A-2])*p[A-1];
            xx = mul*(1-p[A-2])*(1-p[A-1]);

                keepType += uu*(B-A+1);
                keepType += ux*(B-A+1+ B+1);
                keepType += xu*(B-A+1+ B+1);
                keepType += xx*(B-A+1+ B+1);
                keepType += (1-mul)*(B-A+1+ B+1);

          // printf("keepType = %lf\n", keepType);

            backOnce += uu*(2+ B-A+1);
          //  printf("backOnce = %lf\n", backOnce);
            backOnce += ux*(2+ B-A+1);
          //  printf("backOnce = %lf\n", backOnce);
            backOnce += xu*(2+ B-A+1+B+1);
          //  printf("backOnce = %lf\n", backOnce);
            backOnce += xx*(2+ B-A+1+B+1);
         //   printf("backOnce = %lf\n", backOnce);
            backOnce += (1-mul)*(2+B-A+1+B+1);

        //    printf("backOnce = %lf\n", backOnce);
            backTwo += uu*(4+ B-A+1);
            backTwo += ux*(4+ B-A+1);
            backTwo += xu*(4+ B-A+1);
            backTwo += xx*(4+ B-A+1);
            backTwo += (1-mul)*(4+B-A+1+B+1);
           // printf("backTwo = %lf\n", backTwo);

            enRight += uu*(1+ B+1);
            enRight += ux*(1+ B+1);
            enRight += xu*(1+ B+1);
            enRight += xx*(1+ B+1);
            enRight += (1-mul)*(1+ B+1);
            //printf("enRight = %lf\n", enRight);


            ans = keepType;
            if(ans > backOnce) ans = backOnce;
            if(ans > backTwo) ans = backTwo;
            if(ans > enRight) ans = enRight;
        }

        printf("Case #%d: %lf\n", t+1, ans);
    }

}
