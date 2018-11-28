#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;

int O[105],B[105];
int ind1,ind2;
int v[105];
char c[105];
int ret;

int main ()
{
    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");

    int t;

    fscanf (in,"%d",&t);

    for (int id=1; id<=t; id++)
    {
        int n;
        int p1,p2;
        int t1,t2;
        int e1,e2;
        int c1,c2;

        ind1 = ind2 = 0;
        p1 = p2 = 1;
        t1 = t2 = 0;
        ret = 0;

        fscanf (in,"%d ",&n);

        for (int i=0; i<n; i++)
        {
            fscanf (in," %c %d",&c[i],&v[i]);

            if (c[i] == 'O') O[ind1 ++] = v[i];
            else B[ind2 ++] = v[i];
        }
        /// c[n] = '\0';

        for (int i=0; i<n; i++)
        {
            e1 = O[t1];
            e2 = B[t2];

            c1 = (p1 > e1) ? -1 : 1;
            c2 = (p2 > e2) ? -1 : 1;

            if (c[i] == 'O')
            {
                while (p1 != e1)
                {
                    p1 += c1;
                    if (p2 != e2)
                        p2 += c2;
                    ret ++;
                }
                if (p2 != e2)
                    p2 += c2;
                ret ++;
                t1 ++;
            }
            else
            {
                while (p2 != e2)
                {
                    p2 += c2;
                    if (p1 != e1)
                        p1 += c1;
                    ret ++;
                }
                if (p1 != e1)
                    p1 += c1;
                ret ++;
                t2 ++;
            }
        }

        fprintf (out,"Case #%d: %d\n",id,ret);
    }
}
