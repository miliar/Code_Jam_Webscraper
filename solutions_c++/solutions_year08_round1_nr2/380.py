#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MOJO 128
int T[MOJO],X[MOJO][MOJO],Y[MOJO][MOJO];
int mojo[MOJO],resp[MOJO];
int C,N,M,caso;

void dfs(int prof)
{
    if (prof == N)
    {
        int ok,total;

        total = 0;
        for(int i = 0; i < M; i++)
        {
            ok = 0;
            for(int j = 0; j < T[i] && !ok; j++)
                for (int k = 0; k < N && !ok; k++)
                    if (X[i][j] == k && Y[i][j] == mojo[k])
                        ok++;
            if (ok) total++;
        }

        if (total == M)
        {
            if (resp[0] == -1) memcpy(resp,mojo,sizeof(resp));
            else
            {
                int m1,m2;
                m1 = m2 = 0;
                for(int i = 0; i < N; i++)
                {
                    m1 += resp[i];
                    m2 += mojo[i];
                }
                if (m2 < m1) memcpy(resp,mojo,sizeof(resp));
            }
        }

        return;
    }

    for(int i = 0; i < 2; i++)
    {
        mojo[prof] = i;
        dfs(prof+1);
    }
}

int main(void)
{
    for(caso = 1, scanf("%d",&C); caso <= C; caso++)
    {
        scanf("%d %d",&N,&M);
        for(int i = 0; i < M; i++)
        {
            scanf("%d",T+i);
            for(int j = 0; j < T[i]; j++)
            {
                scanf("%d %d",&X[i][j],&Y[i][j]);
                X[i][j]--;
            }
        }

        memset(resp,-1,sizeof(resp));
        dfs(0);

        printf("Case #%d:",caso);
        if (resp[0] == -1) printf(" IMPOSSIBLE");
        else
        {
            for(int i = 0; i < N; i++)
                printf(" %d",resp[i]);
        }
        printf("\n");
    }
    

    return(0);
}

