#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

int P[205];
int V[205];

int main ()
{
    FILE *in = fopen ("B.in","r");
    FILE *out = fopen ("B.out","w");

    int t;

    fscanf (in,"%d",&t);

    for (int ID=1; ID<=t; ID++)
    {
        int C,D;
        double ret = 0;

        fscanf (in,"%d %d",&C,&D);

        for (int i=0; i<C; i++)
            fscanf (in,"%d %d",&P[i],&V[i]);

        double s = 0 , e = 1e9 , m;
        int all = 0;

        while (all ++ < 100)
        {
            m = (s + e) / 2.0;

            double start = P[0] - m;
            double nxt = start + (double)D;

            bool f = 0;

            for (int i=0; i<C; i++)
            {
                int end;
                if (i == 0) end = V[i] - 1;
                else end = V[i];

                int j;

                for (j=0; j<end; j++)
                {
                    double diff = P[i] - nxt;
                    diff = fabs( diff );

                    if ((double)P[i] >= nxt)
                    {
                        if (diff >= m)
                        {
                            nxt = (double)P[i] - m;
                            nxt += (double)D;
                        }
                        else
                            nxt += (double)D;
                    }
                    else
                    {
                        if (diff > m)
                            break;
                        else
                            nxt += (double)D;
                    }
                }

                if (j != end)
                {
                    f = 1;
                    break;
                }
            }

            if (f == 0) e = m , ret = m;
            else s = m;
        }

        fprintf (out,"Case #%d: ",ID);
        fprintf (out,"%lf\n",ret);
    }
}
