#include <stdio.h>
#include <string.h>

int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

int R, C;

char board[102][102], ans[102][102], lastUsed;

bool ok(int r, int c)
{
    return (r >= 0 && r < R && c >= 0 && c < C);   
}

char dfs(int r, int c)
{
    if(ans[r][c] != -1)
    {
        return ans[r][c];    
    }

    int m = 99999, nextR = 0, nextC = 0;
    for(int i = 0; i < 4; ++i)
    {
        int r2 = r + dr[i], c2 = c + dc[i];
        if(ok(r2,c2) && board[r2][c2] < m)
        {
            m = board[r2][c2];
            nextR = r2;
            nextC = c2;
        }
    }
    
    if(m >= board[r][c])
    {
        ans[r][c] = lastUsed;
        ++lastUsed;
        return ans[r][c];   
    }
    
    return ans[r][c] = dfs(nextR, nextC);
}

int main()
{
    freopen("Bsmall.in","r",stdin);
    freopen("Bsmall.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        lastUsed = 'a';
        
        memset(ans,-1,sizeof(ans));
        scanf("%d%d",&R,&C);
        
        for(int i = 0; i < R; ++i)
        for(int j = 0; j < C; ++j)
        scanf("%d",&board[i][j]);   
        
        printf("Case #%d:\n",t);
        for(int r = 0; r < R; ++r)
        {
            for(int c = 0; c < C; ++c)
            {
                if(ans[r][c]==-1)
                {
                    dfs(r,c);
                }   
                printf("%c%s",ans[r][c],c<C-1?" ":"\n");
            }   
        }
        
    }
    return 0;    
}
