#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

long long memx[2][510][510];
long long memy[2][510][510];


int main()
{
    int T;
    scanf("%d",&T);
    for (int num=1;num<=T;++num)
    {
        int R, C, D, ans=0;
        scanf("%d%d%d",&R,&C,&D);
        char w[550][550];
        for (int i=0;i<R;++i)
            scanf("%s",w[i]);
        memset(memx,0,sizeof(memx));
        memset(memy,0,sizeof(memy));
        for (int r=3;r<=max(R,C);++r)
        {
            for (int x=0;x<R-r+1;++x)
                for (int y=0;y<C-r+1;++y)
                {
                    long long curx = memx[r%2][x+1][y+1];
                    long long cury = memy[r%2][x+1][y+1];
                    int cx = x*2+r-1;
                    int cy = y*2+r-1;
                    if (r>3)
                    {
                        curx += ((x+1)*2-cx)*(w[x+1][y+1]-'0' + D);
                        cury += ((y+1)*2-cy)*(w[x+1][y+1]-'0' + D);
                        curx += ((x+r-2)*2-cx)*(w[x+r-2][y+1]-'0' + D);
                        cury += ((y+1)*2-cy)*(w[x+r-2][y+1]-'0' + D);
                        curx += ((x+1)*2-cx)*(w[x+1][y+r-2]-'0' + D);
                        cury += ((y+r-2)*2-cy)*(w[x+1][y+r-2]-'0' + D);
                        curx += ((x+r-2)*2-cx)*(w[x+r-2][y+r-2]-'0' + D);
                        cury += ((y+r-2)*2-cy)*(w[x+r-2][y+r-2]-'0' + D);
                    }
                    for (int i=0;i<r-2;++i)
                    {
                        curx += ((x)*2-cx)*(w[x][y+i+1]-'0'+D);
                        cury += ((y+i+1)*2-cy)*(w[x][y+i+1]-'0'+D);
                        curx += ((x+i+1)*2-cx)*(w[x+i+1][y]-'0'+D);
                        cury += ((y)*2-cy)*(w[x+i+1][y]-'0'+D);
                        curx += ((x+r-1)*2-cx)*(w[x+r-1][y+i+1]-'0'+D);
                        cury += ((y+i+1)*2-cy)*(w[x+r-1][y+i+1]-'0'+D);
                        curx += ((x+i+1)*2-cx)*(w[x+i+1][y+r-1]-'0'+D);
                        cury += ((y+r-1)*2-cy)*(w[x+i+1][y+r-1]-'0'+D);
                    }
                    memx[r%2][x][y] = curx;
                    memy[r%2][x][y] = cury;
                    if (curx==0 && cury==0 && ans<r)
                        ans = r;
                }
        }
        if (ans==0)
            printf("Case #%d: IMPOSSIBLE\n",num);
        else
            printf("Case #%d: %d\n",num,ans);
    }
    return 0;
}
