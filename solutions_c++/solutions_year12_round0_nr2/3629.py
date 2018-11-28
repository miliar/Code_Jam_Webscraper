#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

FILE *in = fopen ("B.in","r");
FILE *out = fopen ("B.out","w");

int main()
{
    int t,n,s,p,g,c=1,i;

    fscanf (in,"%d",&t);

    for (c;c<=t;c++)
    {
        fscanf (in,"%d %d %d",&n,&s,&p);
        int ret=0;
        int x[3];
        for (i=0;i<n;i++)
        {
            fscanf (in,"%d",&g);
            int b=g/3;
            int l=g%3;
            if (b>=p)
            {
                ret++;
                continue;
            }
            if (!l)
            {
               if (b+1>=p&&s&&b)
               {
                  s--;
                  ret++;
               }
            }
            if (l>0)
            {
                if (b+1>=p)
                {
                    ret++;
                    continue;
                }
                if (s&&l==2&&b+2>=p)
                {
                    ret++;
                    s--;
                }
            }
        }
        fprintf (out,"Case #%d: %d\n",c,ret);
    }

    return 0;
}
