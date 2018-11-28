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

int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int c,n;
    int i,j,k;

    int ans[31] = 
    {
        0,
        0,
        27,
        143,
        751,
        935,
        607,
        903,
        991,
        335,
        47,
        943,
        471,
        55,
        447,
        463,
        991,
        95,
        607,
        263,
        151,
        855,
        527,
        743,
        351,
        135,
        407,
        903,
        791,
        135,
        647
    };

    scanf("%d", &c);
    FOR(i,1,c)
    {
        scanf("%d", &n);
        printf("Case #%d: %03d\n", i, ans[n]);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
