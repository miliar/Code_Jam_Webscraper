#include<iostream>
using namespace std;
int R, W;
int H[128][128];
int cur;
int res[128][128];
int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};
bool IN(int y, int x)
{
     return 0 <= y && y < R && 0 <= x && x < W;
}
int main()
{
    int t, cs = 0;
    int i, j, cx, cy, mk, y2, x2;
    freopen("B_L.in", "r", stdin);
    freopen("B_L.out", "w", stdout);
    
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &R, &W);
        for(i = 0; i < R; ++i)
           for(j = 0; j < W; ++j)
               scanf("%d", &H[i][j]);
        cur = 0;
        memset(res, -1, sizeof(res));
        int mh, d;
        for(i = 0; i < R; ++i)
            for(j = 0; j < W; ++j)
            {
                cx = j, cy = i;
                //printf("%d %d\n", i, j);
                while(1)
                {
                    mh = H[cy][cx];
                    for(d = 0; d < 4; ++d)
                    {
                        y2 = cy + dy[d];
                        x2 = cx + dx[d];
                        if(IN(y2, x2) && H[y2][x2] < mh)
                        {
                            mh = H[y2][x2];
                            mk = d;
                        }
                    }
                    if(mh < H[cy][cx])
                    {
                        cx += dx[mk];
                        cy += dy[mk];
                    }
                    else break;
                }
                if(res[cy][cx] == -1)
                {
                    res[cy][cx] = cur++;
                }
                //printf("%d %d\n", cy, cx);
                res[i][j] = res[cy][cx];
            }
        printf("Case #%d:\n", ++cs);
        for(i = 0; i < R; ++i)
            for(j = 0; j < W; ++j)
            {
                printf("%c", res[i][j] + 'a');
                if(j < W - 1) printf(" ");
                else printf("\n");
            }
    }
}
