// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"
#include "algorithm"

#define _USE_MATH_DEFINES
#include "math.h"

#define Input "Sample.txt"
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

int t[110][110];
int r, w, h;

void GetTotal(int r, int c)
{
    if (t[r][c] >=0) return;

    t[r][c] = 0;
    if (r+2 <= h && c+1 <= w) 
    {
        GetTotal(r+2, c+1);
        t[r][c]+= t[r+2][c+1];
    }
    if (r+1 <= h && c+2 <= w) 
    {
        GetTotal(r+1, c+2);
        t[r][c]+= t[r+1][c+2];
    }
    while (t[r][c] > 10007*2) t[r][c]-=10007;
}

int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int n;
    int rock[20][2];
    int i,j,k;

    scanf("%d", &n);
    FOR(i,1,n)
    {
        scanf("%d %d %d", &h, &w, &r);
        memset(t, 255, sizeof(t));
        t[h][w] = 1;
        FOR(j,0,r-1) 
        {
            scanf("%d %d", rock[j], rock[j]+1);
            t[rock[j][0]][rock[j][1]] = 0;
        }
        GetTotal(1, 1);
        
        printf("Case #%d: %d\n", i, t[1][1]%10007);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}