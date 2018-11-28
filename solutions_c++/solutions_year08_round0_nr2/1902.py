#include <stdio.h>
#include <string.h>

#define MOJO 128
#define VOODOO 2048
int pA[MOJO][2],pB[MOJO][2],eA[VOODOO],eB[VOODOO],tA,tB,a,b;

int main(void)
{
    int N,NA,NB,T,caso;

    for(scanf("%d",&N), caso = 1; caso <= N; caso++)
    {
        memset(eA,0,sizeof(eA));
        memset(eB,0,sizeof(eB));

        scanf("%d",&T);
        scanf("%d %d",&NA,&NB);

        int h1,m1,h2,m2;
        for(int i = 0; i < NA; i++)
        {
            scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
            pA[i][0] = h1*60+m1;
            pA[i][1] = h2*60+m2;
        }
        for(int i = 0; i < NB; i++)
        {
            scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
            pB[i][0] = h1*60+m1;
            pB[i][1] = h2*60+m2;
        }

        tA = tB = a = b = 0;
        for(int t = 0; t < 1440; t++)
        {
            a += eA[t];
            b += eB[t];

            for(int i = 0; i < NA; i++)
                if (pA[i][0] == t)
                {
                    if (a == 0) tA++;
                    else a--;
                    eB[pA[i][1]+T]++;
                }

            for(int i = 0; i < NB; i++)
                if (pB[i][0] == t)
                {
                    if (b == 0) tB++;
                    else b--;
                    eA[pB[i][1]+T]++;
                }
        }

        printf("Case #%d: %d %d\n",caso,tA,tB);
    }

    return(0);
}

