#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

int main ()
{   freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);

    int T;
    int a[105];
    scanf ("%d ",&T);
    int n,s,p;
    for (int f =0;f<T;f++)
    {   int cnt =0;
        scanf ("%d %d %d", &n,&s,&p);
        for (int i=0;i<n;i++)
            scanf ("%d",&a[i]);

        for (int i=0;i<n;i++)
        {   if ((a[i]/3 >= p) || ((a[i]/3 == p-1) && (a[i]%3)>=1))
                cnt++;
            else if (s>0 && (((a[i]/3 == p-1) && (a[i]%3)==0 && a[i]>0) || ((a[i]/3 == p-2) && (a[i]%3)==2)))
            {   cnt++; s--;
            }
        }

        printf ("Case #%d: ",f+1);
        printf ("%d\n",cnt);

    }

return 0;
}
