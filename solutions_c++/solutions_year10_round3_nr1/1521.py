/*******************************************\
*                                           *
*   CodeJam 2010    Round 1                 *
*   Rafael Medina (MedinaSoft)              *
*                                           *
\*******************************************/
#include <cstdio>
using namespace std;

int line = 1, tot;

int main ()
{
    int N,test_case,A[1000],B[1000],intersect;
    for (scanf ("%d", &tot); line <= tot; line++) {
        test_case=0;
        for (scanf ("%d", &N); test_case < N; test_case++) {
            scanf ("%d %d", &A[test_case],&B[test_case]);
        }
        intersect=0;
        for (int i=0; i<N-1; i++) {
            for (int j=i+1; j<N; j++) {

                int a1,b1,d1,a2,b2,d2,p,x;
                //b1 and b2 are always 1
                a1 = A[i] - B[i];
                b1 = 1;
                d1 = (b1 * A[i]);

                a2 = A[j] - B[j];
                b2 = 1;
                d2 = (b2 * A[j]);

                //do they intersect or not
                p = (a1 * b2) - (a2 * b1);
                if (p != 0) {
                    x = ( (b2 * d1) - (b1 * d2) ) / p;
                    if (x == 0 || x == 1) { intersect++; }
                }


            }
        }
        printf("Case #%d: %d\n",line,intersect);

        //for (int i=0; i<N; i++) { printf("\t%d %d\n",A[i],B[i]); }
    }

    return 0;
}
