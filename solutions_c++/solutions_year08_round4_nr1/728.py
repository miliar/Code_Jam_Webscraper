// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"
#include "algorithm"

#define _USE_MATH_DEFINES
#include "math.h"

#define Input "sample.txt"
#define Output "Result.txt"

#define MIN(a,b) (a) < (b) ? (a) : (b)
#define MAX(a,b) (a) > (b) ? (a) : (b)
#define IFMIN(a,b) {if ((a) > (b)) a = b;}
#define IFMAX(a,b) {if ((a) < (b)) a = b;}

#define FOR(a,b,c) for (a = b; a <= c; a++)
#define FORB(a,b,c) for (a = b; a >= c; a--)

bool cmp(int a, int b)
{
    return a > b;
}

int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int n;
    int i,j,k;

    int m, V;
    int g[10010], c[10010], v[10010];
    int min[10010][2];

    scanf("%d", &n);
    FOR(i,1,n)
    {
        memset(min, 0, sizeof(min));
        scanf("%d %d", &m, &V);
        FOR(j,1,(m-1)/2) scanf("%d %d", g+j, c+j);
        FOR(j,(m-1)/2+1,m) 
        {
            scanf("%d", v+j);
            min[j][v[j]] = 0;
            min[j][1-v[j]] = m + 1;
        }

        FORB(j,(m-1)/2,1)
        {
            int l = j*2, r = l+1;
            
            if (1 == g[j])
            {
                min[j][0] = MIN(min[l][0] + min[r][0], MIN(min[l][1] + min[r][0], min[l][0] + min[r][1]));
                min[j][1] = min[l][1] + min[r][1];
            }
            else
            {
                min[j][0] = min[l][0] + min[r][0];
                min[j][1] = MIN(min[l][1] + min[r][1], MIN(min[l][1] + min[r][0], min[l][0] + min[r][1]));
            }

            if (1 == c[j])
            {
                if (0 == g[j])
                {
                    IFMIN(min[j][0], MIN(min[l][0] + min[r][0], MIN(min[l][1] + min[r][0], min[l][0] + min[r][1])) + 1);
                    IFMIN(min[j][1], min[l][1] + min[r][1] + 1);
                }
                else
                {
                    IFMIN(min[j][0], min[l][0] + min[r][0] + 1);
                    IFMIN(min[j][1], MIN(min[l][1] + min[r][1], MIN(min[l][1] + min[r][0], min[l][0] + min[r][1])) + 1);
                }
            }

            IFMIN(min[j][0], m + 1);
            IFMIN(min[j][1], m + 1);
        }
        
        if (min[1][V] <= m) printf("Case #%d: %d\n", i, min[1][V]);
        else printf("Case #%d: IMPOSSIBLE\n", i);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
