#include <cstdio>
#include <iostream>

using namespace std;
int main ()
{

    int T,A,B,i,j;
    double p[100000],probability,expected,min;
    scanf("%d",&T);

    for (i=1 ; i<=T  ;i++)
    {
        scanf("%d %d",&A,&B);

        for (j=0 ; j<A ; j++)
        {
            scanf("%lf",&p[j]);
        }
        min = (B+2) * 1.0;
        probability = 1;
        for (j=0 ; j<A ; j++)
        {
            probability *= p[j];
            expected = probability*(A+B-2*j-1)+(1-probability)*(A+2*B-2*j);
            if (expected < min)
            {
                min = expected;
            }
        }
        printf("Case #%d: %.6lf\n",i,min);
    }
    return 0;
}