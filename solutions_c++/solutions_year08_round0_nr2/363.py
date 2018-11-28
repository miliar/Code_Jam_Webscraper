// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"

#define Input "sample.txt"
#define Output "Result.txt"

int ReadTime()
{
    int h, m;
    scanf("%d:%d", &h, &m);
    return m + h * 60;
}

void swap(int &a, int &b)
{
    int c = a;
    a = b;
    b = c;
}

void sort(int A[][2], int t)
{
    int j, k;
    for (j = 0; j < t; j++)
        for (k = j + 1; k < t; k++) 
            if (A[j][0] > A[k][0]
                || (A[j][0] == A[k][0] && A[j][1] < A[k][1]))
            {
                swap(A[j][0], A[k][0]);
                swap(A[j][1], A[k][1]);
            }
}

int Min(int A[][2], int t)
{
    int i, cur = 0, min = 0;

    for (i = 0; i < t; i++)
    {
        cur += A[i][1];
        if (cur < 0)
        {
            cur++;
            min++;
        }
    }
    return min;
}

int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int n, t, na, nb;
    int i,j,k;
    int A[210][2], B[210][2];

    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        scanf("%d %d %d", &t, &na, &nb);
        for (j = 0; j < na; j++)
        {
            A[j][0] = ReadTime();
            A[j][1] = -1;
            B[j][0] = ReadTime() + t;
            B[j][1] = 1;
        }
        for (j = 0; j < nb; j++)
        {
            B[na + j][0] = ReadTime();
            B[na + j][1] = -1;
            A[na + j][0] = ReadTime() + t;
            A[na + j][1] = 1;
        }

        sort(A, na + nb);
        sort(B, na + nb);

        printf("Case #%d: %d %d\n", i, Min(A, na + nb), Min(B, na + nb));
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
