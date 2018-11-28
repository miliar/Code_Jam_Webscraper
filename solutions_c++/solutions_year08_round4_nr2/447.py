#include <stdio.h>

int main(void)
{
    int C,N,M,A,caso;

    for(scanf("%d",&C), caso = 1; caso <= C; caso++)
    {
        int x[3],y[3],ok;

        scanf("%d %d %d",&N,&M,&A);
        printf("Case #%d: ",caso);
        ok = 0;

        x[0] = y[0] = 0;
        for(x[1] = 0;  x[1] <= N && !ok; x[1]++)
            for(x[2] = 0; x[2] <= N && !ok; x[2]++)
                for(y[1] = 0; y[1] <= M && !ok; y[1]++)
                    for(y[2] = 0; y[2] <= M && !ok; y[2]++)
                    {
                        int area;

                        area = x[1]*y[0]-x[0]*y[1];
                        area += x[2]*y[1]-x[1]*y[2];
                        area += x[0]*y[2]-x[2]*y[0];

                        if (area == A || -area == A)
                        {
                            printf("%d %d %d %d %d %d\n",x[0],y[0],x[1],y[1],x[2],y[2]);
                            ok = 1;
                        }
                    }

        if (!ok) printf("IMPOSSIBLE\n");
    }

    return(0);
}

