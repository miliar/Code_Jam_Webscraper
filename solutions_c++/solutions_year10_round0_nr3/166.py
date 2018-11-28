#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long huge;

#define MAX 1024
huge foi[MAX],g[MAX],S[MAX];

int main(void)
{
    int N,k,R,T,caso;

    for(scanf("%d",&T), caso = 1; caso <= T; caso++)
    {
        scanf("%d %d %d",&R,&k,&N);
        for(int i = 0; i < N; i++)
            scanf("%lld",g+i);

        if (N == 1)
        {
            printf("Case #%d: %lld\n",caso,g[0]*R);
            continue;
        }

        int fim = 1;
        int soma = g[0];
        for(int i = 0; i < N; i++)
        {
            while(g[fim]+soma <= k)
            {
                soma += g[fim];
                fim = (fim+1)%N;
                if (fim == i)
                    break;
            }
            foi[i] = fim;
            S[i] = soma;
            soma -= g[i];
        }

        /*
        for(int i = 0; i < N; i++)
            printf("%d [%d %d]\n",i,foi[i],S[i]);
        */

        huge r = 0;
        int j = 0;
        for(int i = 0; i < R; i++)
        {
            r += S[j];
            j = foi[j];
        }

        printf("Case #%d: %lld\n",caso,r);

    }

    return(0);
}

