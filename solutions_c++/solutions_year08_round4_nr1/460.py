#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MOJO 10100
#define oo 0x3f3f3f3f
int G[MOJO],C[MOJO],I[MOJO],voodoo[MOJO][2];
int M,V;

int voodoo_doll(int n, int v)
{
    int &mojo = voodoo[n][v];

    if (I[n] > -1)
        mojo = (I[n] == v) ? 0 : +oo;

    if (mojo < 0)
    {
        mojo = +oo;

        voodoo_doll(2*n,1);
        voodoo_doll(2*n+1,1);
        voodoo_doll(2*n,0);
        voodoo_doll(2*n+1,0);

        // and
        if (G[n] == 1)
        {
            if (v == 1)
            {
                mojo = min(mojo,voodoo[2*n][1]+voodoo[2*n+1][1]);
            }
            else
            {
                mojo = min(mojo,voodoo[2*n][1]+voodoo[2*n+1][0]);
                mojo = min(mojo,voodoo[2*n][0]+voodoo[2*n+1][1]);
                mojo = min(mojo,voodoo[2*n][0]+voodoo[2*n+1][0]);
            }
            if (C[n] == 1)
            {
                if (v == 1)
                {
                    mojo = min(mojo,voodoo[2*n][1]+voodoo[2*n+1][0]+1);
                    mojo = min(mojo,voodoo[2*n][0]+voodoo[2*n+1][1]+1);
                    mojo = min(mojo,voodoo[2*n][1]+voodoo[2*n+1][1]+1);
                }
                else
                {
                    mojo = min(mojo,voodoo[2*n][0]+voodoo[2*n+1][0]+1);
                }
            }
        }
        // or
        else
        {
            if (v == 1)
            {
                mojo = min(mojo,voodoo[2*n][1]+voodoo[2*n+1][0]);
                mojo = min(mojo,voodoo[2*n][0]+voodoo[2*n+1][1]);
                mojo = min(mojo,voodoo[2*n][1]+voodoo[2*n+1][1]);
            }
            else
            {
                mojo = min(mojo,voodoo[2*n][0]+voodoo[2*n+1][0]);
            }

            if (C[n] == 1)
            {
                if (v == 1)
                {
                    mojo = min(mojo,voodoo[2*n][1]+voodoo[2*n+1][1]+1);
                }
                else
                {
                    mojo = min(mojo,voodoo[2*n][1]+voodoo[2*n+1][0]+1);
                    mojo = min(mojo,voodoo[2*n][0]+voodoo[2*n+1][1]+1);
                    mojo = min(mojo,voodoo[2*n][0]+voodoo[2*n+1][0]+1);
                }
            }
        }
    }

    return(mojo);
}

int main(void)
{
    int caso,N;

    for(caso = 1, scanf("%d",&N); caso <= N; caso++)
    {
        scanf("%d %d",&M,&V);
        memset(I,-1,sizeof(I));
        for(int i = 0; i < M; i++)
        {
            if (i < (M-1)/2)
                scanf("%d %d",G+i+1,C+i+1);
            else scanf("%d",I+i+1);
        }

        printf("Case #%d: ",caso);

        memset(voodoo,-1,sizeof(voodoo));
        voodoo_doll(1,V);
        if (voodoo[1][V] < +oo) printf("%d\n",voodoo[1][V]);
        else printf("IMPOSSIBLE\n");
    }

    return(0);
}
