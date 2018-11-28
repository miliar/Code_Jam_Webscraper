// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"

#define _USE_MATH_DEFINES
#include "math.h"

#define Input "sample.txt"
#define Output "Result.txt"

#define MIN(a,b) (a) < (b) ? (a) : (b)
#define MAX(a,b) (a) > (b) ? (a) : (b)
#define IFMIN(a,b) {if ((a) > (b)) a = b;}
#define IFMAX(a,b) {if ((a) < (b)) a = b;}

#define FOR(a,b,c) for (a = b; a <= c; a++)

int p[2010][2010][2];
int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int c,n,m;
    int b[2010], t[2010];
    int left;
    int i,j,k,h,temp;

    scanf("%d", &c);
    FOR(i,1,c)
    {
        scanf("%d %d", &n, &m);
        left = 0;
        FOR(j,0,m-1)
        {
            scanf("%d", t+j);
            FOR(k,0,t[j]-1)
            {
                scanf("%d %d", p[j][k], p[j][k]+1);
                if (1 == p[j][k][1])
                {
                    left++;
                    if (k > 0)
                    {
                        p[j][k][1] = 0;
                        p[j][0][1] = 1;
                        temp = p[j][0][0];
                        p[j][0][0] = p[j][k][0];
                        p[j][k][0] = temp;
                    }
                }
            }
        }

        memset(b, 0, sizeof(b));
        do
        {
            bool fFound = false;
            FOR(j,0,m-1) if (1 == t[j] && 1 == p[j][0][1])
            {
                fFound = true;
                temp = p[j][0][0];
                b[temp-1] = 1;
                FOR(k,0,m-1) if (t[k] > 0 && 1 == p[k][0][1] && temp == p[k][0][0])
                {
                    left--;
                    t[k] = 0;
                }

                FOR(k,0,m-1) 
                    FOR(h,0,t[k]-1) if (p[k][h][0] == temp)
                        if (--t[k] > 0) p[k][h][0] = p[k][t[k]][0];
                        else 
                        {
                            left = 1;
                            goto IMPOSSIBLE;
                        }
            }
            if (!fFound) left = 0;
        }
        while (left > 0);

IMPOSSIBLE:
        printf("Case #%d:", i);
        if (left > 0) printf(" IMPOSSIBLE");
        else
        {
            FOR(j,0,n-1) printf(" %d", b[j]);
        }
        printf("\n");
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
