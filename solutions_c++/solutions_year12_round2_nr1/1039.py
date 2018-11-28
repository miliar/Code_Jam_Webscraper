#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;

map < int , double > m;

int main ()
{
    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");

    int t;
    int k = 1;

    fscanf (in,"%d",&t);

    while( t -- )
    {
        fprintf (out,"Case #%d:",k);
        k ++;

        m.clear();

        int n;
        int arr[1005],a[1005];
        int sum = 0 , mx = -1 , mn = 1<<30;

        fscanf (in,"%d",&n);
        for (int i=0; i<n; i++)
        {
            fscanf (in,"%d",&arr[i]);
            a[i] = arr[i];
            sum += arr[i];
        }

        sort (arr,arr+n);
        reverse (arr,arr+n);

        int start = 0;

        while( start < n-1 )
        {
            mx = -1 , mn = 1<<30;

            mx = arr[start];
            mn = arr[n-1];

            double s = mx , e = mx + sum , mid;
            int cnt = 0;
            double ret;

            while( cnt ++ < 100 )
            {
                double all = 0;

                mid = (s + e) / 2.0;
                for (int i=start; i<n; i++)
                {
                    double val = (mid - arr[i]) / (double)sum;
                    all += val;
                }

                if (all >= 1) e = mid , ret = mid;
                else s = mid;
            }

            double chk = 0;

            for (int i=start; i<n; i++)
            {
                double val = (ret - arr[i]) / (double)sum;
                chk += val;
            }

            if (chk - 1 < 1e-5)
            {
                for (int i=0; i<n; i++)
                {
                    double val = (ret - arr[i]) / (double)sum;
                    if (i < start) val = 0;
                    val = val * 100.0;
                    m[arr[i]] = val;
                }
                break;
            }
            else
                start ++;
        }

        for (int i=0; i<n; i++)
        {
            fprintf (out, " ");
            fprintf (out,"%lf",m[a[i]]);
        }

        fprintf (out,"\n");
    }
}
