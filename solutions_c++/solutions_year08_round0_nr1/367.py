// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"

#define Input "sample.txt"
#define Output "Result.txt"

int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int n, s, q;
    int i,j,k,h;

    char temp[110];
    char Name[110][110];
    int Query[1010];
    int Min[1010][110];
    
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        scanf("%d", &s);
        scanf("%c", temp);
        for (j = 0; j < s; j++)
        {
            scanf("%[^\n]", Name[j]);
            scanf("%c", temp);
        }

        scanf("%d", &q);
        scanf("%c", temp);
        for (j = 1; j <= q; j++)
        {
            scanf("%[^\n]", temp);
            Query[j] = 0;
            for (k = 0; k < s; k++)
                if (0 == strcmp(temp, Name[k]))
                {
                    Query[j] = k;
                    break;
                }
            scanf("%c", temp);
        }

        memset(Min, 0, sizeof(Min));
        if (q > 0) Min[q][Query[q]] = 1;
        for (j = q-1; j >= 0; j--)
        {
            for (k = 0; k < s; k++)
                if (Query[j] != k) Min[j][k] = Min[j+1][k];
                else
                {
                    Min[j][k] = Min[j+1][k] + 2;
                    for (h = 0; h < s; h++)
                        if (h != k && Min[j][k] > Min[j+1][h] + 1) Min[j][k] = Min[j+1][h] + 1;
                }            
        }

        k = 0;
        for (j = 1; j < s; j++) if (Min[0][k] > Min[0][j]) k = j;
        printf("Case #%d: %d\n", i, Min[0][k]);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
