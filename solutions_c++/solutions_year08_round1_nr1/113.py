// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#define _USE_MATH_DEFINES
#include "math.h"

#define Input "sample.txt"
#define Output "Result.txt"

#define MIN(a,b) (a) < (b) ? (a) : (b)
#define MAX(a,b) (a) > (b) ? (a) : (b)
#define IFMIN(a,b) {if ((a) > (b)) a = b;}
#define IFMAX(a,b) {if ((a) < (b)) a = b;}

#define FOR(a,b,c) for (a = b; a <= c; a++)

void Sort1(long a[], int t)
{
    int i,j;
    long temp;
    FOR(i, 0, t-1)
        FOR(j, i+1, t-1) if (a[i] > a[j]) 
    {
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}

void Sort2(long a[], int t)
{
    int i,j;
    long temp;
    FOR(i, 0, t-1)
        FOR(j, i+1, t-1) if (a[i] < a[j]) 
    {
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int n,t;
    int i,j,k;

    long x[810], y[810];
    long long sum;

    scanf("%d", &n);
    FOR(i,1,n)
    {
        scanf("%d", &t);
        FOR(j,0,t-1) scanf("%I64d", x+j);
        FOR(j,0,t-1) scanf("%d", y+j);
        Sort1(x, t);
        Sort2(y, t);
        sum = 0;
        FOR(j,0,t-1) sum+= ((long long)x[j])*y[j];
        printf("Case #%d: %I64d\n", i, sum);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
