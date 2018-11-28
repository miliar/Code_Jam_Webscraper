

#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
int bg[10][10];
int sm[10][10];

int main()
{
      freopen ("D.in","r",stdin);
      freopen ("small.op","w",stdout);

    //  freopen ("C2.in","r",stdin);
    //  freopen ("large.op","w",stdout);
    int t, c = 0;
    scanf("%d", &t);
    while (t--)
    {
        int op;
        int v[10];
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                bg[i][j] = sm[i][j] = 0;
            }

            
        }

        for (int i = 0; i < n - 1; i++)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            a--;
            b--;
            bg[a][b] = 1;
            bg[b][a] = 1;
        }
        int m;
        scanf("%d", &m);
        for (int i = 0; i < m - 1; i++)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            a--;
            b--;
            sm[a][b] = sm[b][a] = 1;
        }
        
        for (int i = 0; i < n; i++)
        {
            v[i]=i;
        }
        bool pos = false;
        do
        {
            bool ppos = true;
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (sm[i][j])
                    {
                        if (!bg[v[i]][v[j]])
                        {
                            ppos = false;
                            break;
                        }
                    }
                }
                

            }
            if (ppos)
                {
                    pos = true;
                    break;
                }

        }
        while (next_permutation(v, v+n));
        
        if (pos)
            printf("Case #%d: YES\n", ++c);
        else
            printf("Case #%d: NO\n", ++c);
    }
    return 0;
}

