#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main ()
{
    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");

    int t;

    fscanf (in,"%d",&t);

    for (int ID=1; ID<=t; ID++)
    {
        int r,c;
        char mp[55][55];

        fscanf (in,"%d %d",&r,&c);
        for (int i=0; i<r; i++)
            fscanf (in,"%s",mp[i]);

        for (int i=0; i<r; i++)
        {
            for (int j=0; j<c; j++)
            {
                int cnt = 0;

                if (mp[i][j] == '#')
                {
                    if (i+1 < r && mp[i+1][j] == '#') cnt ++;
                    if (j+1 < c && mp[i][j+1] == '#') cnt ++;
                    if (i+1 < r && j+1 < c && mp[i+1][j+1] == '#') cnt ++;

                    if (cnt == 3)
                    {
                        mp[i][j] = mp[i+1][j+1] = '/';
                        mp[i+1][j] = mp[i][j+1] = '\\';
                    }
                }
            }
        }

        bool f = 0;

        for (int i=0; i<r; i++)
        {
            for (int j=0; j<c; j++)
            {
                if (mp[i][j] == '#')
                {
                    f = 1;
                    break;
                }
            }
        }

        fprintf (out,"Case #%d:\n",ID);
        if (f == 1) fprintf (out,"Impossible\n");
        else
        {
            for (int i=0; i<r; i++)
                fprintf (out,"%s\n",mp[i]);
        }
    }
}
