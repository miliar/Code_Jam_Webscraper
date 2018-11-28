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

int Num2Row(int num, int n, int* r)
{
    int i, t=0;
    FOR(i,0,n-1) 
        if (num & (1<<i)) r[i] = 1, t++; else r[i] = 0;
    return t;
}

int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int c,m,n;
    char room[100][100];
    int r1[20], r2[20];
    int max[100][2000];
    int i,j,k,h,t;

    scanf("%d", &c);
    FOR(i,1,c)
    {
        scanf("%d %d", &m, &n);
        FOR(j,1,m) scanf("%s", room[j]);

        memset(max,0,sizeof(max));
        FORB(j,m,0)
        {
            FOR(k,0,(1<<n)-1)
            {
                max[j][k]=-1;
                
                t=Num2Row(k, n, r1);
                FOR(h,0,n-1) if (r1[h] && room[j][h]=='x') break;
                if (h<n) continue;

                FOR(h,1,n-1) if (r1[h] && r1[h-1]) break;
                if (h<n) continue;

                FOR(h,0,n-2) if (r1[h] && r1[h+1]) break;
                if (h<n-1) continue;

                FOR(h,0,(1<<n)-1) if (max[j+1][h]>=0)
                {
                    if ((k & (h<<1)) || (k & (h>>1))) continue;
                    IFMAX(max[j][k], max[j+1][h]);
                }
                if (max[j][k]>=0) max[j][k]+=t;
            }
        }
        printf("Case #%d: %d\n", i, max[0][0]);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}