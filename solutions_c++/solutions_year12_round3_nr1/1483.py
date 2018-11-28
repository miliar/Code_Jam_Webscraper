#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

int sum[1005][1005];
int n,m;
vector < vector <int> > v;

void solve (int ind , int start)
{
    sum[start][ind] ++;

    for (int i=0; i<v[ind].size(); i++)
        solve (v[ind][i] , start);

    return;
}

int main ()
{
    int t;
    int k = 1;

    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");

    fscanf (in,"%d",&t);

    while (t --)
    {
        fprintf (out,"Case #%d: ",k);
        k ++;

        memset (sum,0,sizeof(sum));

        fscanf (in,"%d",&n);

        v.clear();
        v.resize( n + 2 );

        for (int i=0; i<n; i++)
        {
            int m;
            fscanf (in,"%d",&m);

            for (int j=0; j<m; j++)
            {
                int a;
                fscanf (in,"%d",&a);
                v[i].push_back( a-1 );
            }
        }

        for (int i=0; i<n; i++)
            solve (i,i);

        bool f = 0;

        for (int i=0; i<n; i++)
        {
            for (int j=0; j<n; j++)
            {
                if (i == j) continue;
                if (sum[i][j] > 1)
                {
                    f = 1;
                    fprintf (out,"Yes");
                    break;
                }
            }
            if (f == 1)
                break;
        }

        if (f == 0) fprintf (out,"No");
        fprintf (out,"\n");
    }
}
