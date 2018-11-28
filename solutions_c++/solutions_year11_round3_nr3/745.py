#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main ()
{
    FILE *in = fopen ("C.in","r");
    FILE *out = fopen ("C.out","w");

    int t;

    fscanf (in,"%d",&t);

    for (int ID=1; ID<=t; ID++)
    {
        int n,L,H;
        int arr[105];

        fscanf (in,"%d %d %d",&n,&L,&H);
        for (int i=0; i<n; i++)
            fscanf (in,"%d",&arr[i]);

        fprintf (out,"Case #%d: ",ID);

        bool f = 0;

        for (int i=L; i<=H; i++)
        {
            int j;
            for (j=0; j<n; j++)
            {
                if (i % arr[j] == 0 || arr[j] % i == 0) continue;
                else break;
            }
            if (j == n)
            {
                f = 1;
                fprintf (out,"%d\n",i);
                break;
            }
        }

        if (f == 0) fprintf (out,"NO\n");
    }
}
