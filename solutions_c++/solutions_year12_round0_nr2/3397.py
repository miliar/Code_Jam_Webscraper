#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int arr[105][5];
int score[105];

int main ()
{
    FILE *in = fopen ("B.in","r");
    FILE *out = fopen ("B.out","w");

    int t;
    int k = 1;

    fscanf (in,"%d",&t);

    while( t -- )
    {
        int ret = 0;
        int n,s,p;

        memset (arr,0,sizeof(arr));

        fscanf (in,"%d %d %d",&n,&s,&p);
        for (int i=0; i<n; i++)
            fscanf (in,"%d",&score[i]);

        for (int i=0; i<n; i++)
        {
            arr[i][0] = score[i] / 3;
            arr[i][1] = (score[i] - arr[i][0]) / 2;
            arr[i][2] = (score[i] - arr[i][0] - arr[i][1]) / 1;
            sort( arr[i] , arr[i]+3 );
        }

        for (int i=0; i<n; i++)
        {
            if (arr[i][2] >= p)
                ret ++;
            else
            {
                if (arr[i][1] == 0)
                    continue;
                if (arr[i][2] + 1 == p && s > 0 && arr[i][2] - arr[i][1] == 0)
                {
                    ret ++;
                    s --;
                }
            }
        }

        fprintf (out,"Case #%d: %d\n",k,ret);
        k ++;
    }
}
