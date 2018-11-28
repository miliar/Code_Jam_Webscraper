#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

double arr[105];

int main ()
{
    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");

    int t;

    fscanf (in,"%d",&t);

    for (int ID=1; ID<=t; ID++)
    {
        int n;
        char c[105][105];

        fscanf (in,"%d",&n);
        for (int i=0; i<n; i++)
            fscanf (in,"%s",c[i]);

        fprintf (out,"Case #%d:\n",ID);

        for (int i=0; i<n; i++)
        {
            double F = 0;
            int cnt = 0;

            for (int j=0; j<n; j++)
            {
                int OCw = 0;
                int OCa = 0;

                if (c[i][j] == '.') continue;

                for (int p=0; p<n; p++)
                {
                    if (p == i) continue;

                    if (c[j][p] == '1') OCw ++ , OCa ++;
                    else if (c[j][p] == '0') OCa ++;
                }

                F += (double)OCw / OCa;
                cnt ++;
            }

            arr[i] = F / cnt;
        }

        for (int i=0; i<n; i++)
        {
            double WP = 0;
            double OWP = 0;
            double OOWP = 0;

            int Cw = 0;
            int Ca = 0;

            double S = 0;
            int cnt = 0;

            for (int j=0; j<n; j++)
            {
                if (c[i][j] == '1') Cw ++ , Ca ++;
                else if (c[i][j] == '0') Ca ++;
                else continue;

                S += arr[j];
                cnt ++;
            }

            WP = (double)Cw / Ca;
            OWP = arr[i];
            OOWP = S / cnt;

            double ret = (0.25 * WP) + (0.5 * OWP) + (0.25 * OOWP);
            fprintf (out,"%lf\n",ret);
        }
    }
}
