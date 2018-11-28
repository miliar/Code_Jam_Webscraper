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

    int n,k;
    int i,j,h,l;

    char s[50010], c[50010];
    int p[20];
    int min;
    
    scanf("%d", &n);
    FOR(i,1,n)
    {
        scanf("%d %s", &k, s);
        l = strlen(s); min = l;

        FOR(j,0,k-1) p[j]=j;
        
        do
        {
            //FOR(j,0,k-1) printf("%d ",p[j]); printf("\n");
            
            j=0;
            while(j<l)
            {
                FOR(h,0,k-1) c[j+h]=s[j+p[h]];
                j+=k;
            }
            c[l]=0;
            //printf("%s\n", c);

            j=0; h=0;
            while(j<l)
            {
                while(c[j]==c[j+1]) j++;
                h++;
                j++;
            }
            IFMIN(min, h);
        } while (std::next_permutation(p, p + k));

        printf("Case #%d: %d\n", i, min);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
