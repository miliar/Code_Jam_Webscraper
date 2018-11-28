#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main ()
{
    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");

    int t;
    int k = 1;

    fscanf (in,"%d",&t);

    while( t -- )
    {
        double ret = 0 , f = 1;
        double arr[5];
        int a,b;

        fscanf (in,"%d %d",&a,&b);
        for (int i=0; i<a; i++)
        {
            fscanf (in,"%lf",&arr[i]);
            f *= arr[i];
        }

        ret = b + 2;
        ret = min( ret , f * ( b - a + 1 ) + ( 1.0 - f ) * ( b - a + 1 + b + 1 ) );

        for (int bc=1; bc<=a; bc++)
        {
            double ans = 0;
            for (int i=0; i<(1<<a); i++)
            {
                f = 1;
                for (int j=0; j<a; j++)
                {
                    if (i & (1<<j)) f *= 1.0 - arr[j];
                    else f *= arr[j];
                }

                bool v = 0;
                for (int j=0; j<a-bc; j++)
                {
                    if (i & (1<<j))
                    {
                        v = 1;
                        break;
                    }
                }

                if (v == 1) ans += ( bc + (b - a + bc) + 1 + b + 1 ) * f;
                else ans += ( bc + (b - a + bc) + 1 ) * f;
            }
            ret = min( ret , ans );
        }

        fprintf (out,"Case #%d: ",k);
        k ++;

        fprintf (out,"%lf\n",ret);
    }
}
