#include <stdio.h>
#include <algorithm>

using namespace std;

#define MOJO 256
#define MOD 10007

int N,H,W,R,b[MOJO][MOJO],voodoo[MOJO][MOJO];

int voodoo_doll(int r, int c)
{
    int &mojo = voodoo[r][c];

    if (r >= H || c >= W) mojo = 0;
    else if (b[r][c] == 1) mojo = 0;

    if (mojo < 0)
    {
        voodoo_doll(r+2,c+1);
        voodoo_doll(r+1,c+2);
        mojo = (voodoo[r+2][c+1]+voodoo[r+1][c+2])%MOD;
    }

    return(mojo);
}

int main(void)
{
    int caso;

    for(caso = 1, scanf("%d",&N); caso <= N; caso++)
    {
        scanf("%d %d %d",&H,&W,&R);

        memset(b,0,sizeof(b));
        memset(voodoo,-1,sizeof(voodoo));

        for(int i = 0; i < R; i++)
        {
            int r,c;
            scanf("%d %d",&r,&c);
            b[r-1][c-1] = 1;
        }

        voodoo[H-1][W-1] = 1;
        voodoo_doll(0,0);
        printf("Case #%d: %d\n",caso,voodoo[0][0]);
    }

    return(0);
}

