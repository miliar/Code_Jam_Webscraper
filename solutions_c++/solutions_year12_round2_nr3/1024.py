#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
using namespace std;

map <int , int> m;
vector <int> v;

int main ()
{
    int t;
    int k = 1;

    FILE *in = fopen ("C.in","r");
    FILE *out = fopen ("C.out","w");

    fscanf (in,"%d",&t);

    while( t -- )
    {
        fprintf (out,"Case #%d:\n",k);
        k ++;

        int n;
        int arr[25];

        m.clear();

        fscanf (in,"%d",&n);
        for (int i=0; i<n; i++)
            fscanf (in,"%d",&arr[i]);

        int ret;

        for (int i=0; i<(1<<n); i++)
        {
            int sum = 0;

            for (int j=0; j<n; j++)
            {
                if (i & (1<<j))
                    sum += arr[j];
            }

            if (m[sum] >= 1)
            {
                ret = sum;
                break;
            }
            else
                m[sum] ++;
        }

        v.clear();

        int f = 0;

        for (int i=0; i<(1<<n); i++)
        {
            int sum = 0;

            for (int j=0; j<n; j++)
            {
                if (i & (1<<j))
                    sum += arr[j];
            }

            if (sum == ret && f < 2)
            {
                f ++;
                for (int j=0; j<n; j++)
                {
                    if (i & (1<<j))
                        v.push_back( arr[j] );
                }
                for (int j=0; j<v.size(); j++)
                {
                    if (j != 0) fprintf (out," ");
                    fprintf (out,"%d",v[j]);
                }
                fprintf (out,"\n");
                v.clear();
            }
        }

        if (f == 0)
            fprintf (out,"Impossible\n");
    }
}
