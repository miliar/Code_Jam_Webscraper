#include <stdio.h>
#include <string.h>

struct ENGINE 
{
    char szEngine[128];
    bool bUse;
};

ENGINE aEngine[101];
char  aQuery[1001][128];
int T, S, Q;
int nMin;

void solve()
{
    int i, j, k, t;

    nMin = 0;
    t = 0;
    for (i = 0; i < Q; ++i)
    {
        for (j = 0; j < S; ++j)
        {
            if (!aEngine[j].bUse && strcmp(aEngine[j].szEngine, aQuery[i]) == 0)
            {
                aEngine[j].bUse = true;
                t = j;
            }
        }
        for (k = 0; k < S; ++k)
        {
            if (!aEngine[k].bUse)
                break;
        }
        if (k == S)
        {
            ++nMin;
            for (k = 0; k < S; ++k)
                aEngine[k].bUse = false;
            aEngine[t].bUse = true;
        }
    }
}

int main()
{
    int i, j;

    scanf("%d", &T);
    for (i = 1; i <= T; ++i)
    {
        scanf("%d", &S);
        getchar();
        for (j = 0; j < S; ++j)
        {
            gets(aEngine[j].szEngine);
            aEngine[j].bUse = false;
        }

        scanf("%d", &Q);
        getchar();
        for (j = 0; j < Q; ++j)
        {
            gets(aQuery[j]);
        }
        
        solve();

        printf("Case #%d: %d", i, nMin);
        if (i != T)
            printf("\n");
    }
    return 0;
}
