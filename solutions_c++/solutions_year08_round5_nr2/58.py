#include <cstdio>
#include <queue>
#include <utility>
#include <cstring>
using namespace std;

typedef pair<int, int> Loc;

struct
{
    int x, y;      
}dif[] = {-1, 0, 1, 0, 0, 1, 0, -1};
int main()
{
    int N;
    scanf("%d", &N);
    
    
    char map[32][32];
    for(int z = 1; z <= N; z++)
    {
        memset(map, '#', sizeof(map));
        int R, C;
        scanf("%d%d", &R, &C);
        
        char buf[32];
        fgets(buf, 32, stdin);
        for(int i = 1; i <= R; i++)
        {
            fgets(map[i] + 1, 32, stdin);
            map[i][C + 1] = '#';
        }
            
        
        int towall[32][32];
        
        Loc start;
        Loc cake;
        for(int i = 1; i <= R; i++)
            for(int j = 1; j <= C; j++)
                if(map[i][j] != '#')
                {               
                    queue<pair<int, int> > que;
            
                    que.push(make_pair(i, j));
                    
                    if(map[i][j] == 'O')
                        start = make_pair(i, j);
                    if(map[i][j] == 'X')
                        cake = make_pair(i, j);
                    
                    bool pass[32][32] = {0};
                    pass[i][j] = true;
                    
                    try
                    {
                    for(int step = 0; que.size(); step++)
                        for(int ts = que.size(); ts > 0; ts--)                        
                        {
                            Loc p = que.front();
                            que.pop();
                        
                            for(int d = 0; d < 4; d++)
                            {
                                int nx = p.first + dif[d].x;
                                int ny = p.second + dif[d].y;
                            
                                if(map[nx][ny] == '#')
                                {
                                    towall[i][j] = step + 1;
                                    throw 0;               
                                }
                                
                                pass[nx][ny] = true;
                                que.push(make_pair(nx, ny));
                            }
                        
                        }
                    }
                    catch(...)
                    {}
                    
                }
            
        
        
        int ans[32][32];
        for(int i = 1; i <= R; i++)
            for(int j = 1; j <= C; j++)
                ans[i][j] = INT_MAX;
                
        ans[start.first][start.second] = 0;
        
        queue<Loc> update;
        update.push(start);
        bool inque[32][32] = {0};
        
        inque[start.first][start.second] = true;
        while(update.size())
        {
            Loc p = update.front();
            update.pop();
            inque[p.first][p.second] = false;
                         
            for(int d = 0; d < 4; d++)
            {
                int nx = p.first + dif[d].x;
                int ny = p.second + dif[d].y;
                
                if(map[nx][ny] != '#')
                {
                    if(ans[nx][ny] > ans[p.first][p.second] + 1)
                    {
                        ans[nx][ny] = ans[p.first][p.second] + 1;
                        if(!inque[nx][ny])
                        {
                            update.push(make_pair(nx, ny));
                            inque[nx][ny] = true;                  
                        }
                    }
                    
                    while(map[nx + dif[d].x][ny + dif[d].y] != '#')
                    {
                        nx += dif[d].x;
                        ny += dif[d].y;
                    }
                    
                    if(ans[nx][ny] > ans[p.first][p.second] + towall[p.first][p.second])
                    {
                        ans[nx][ny] = ans[p.first][p.second] + towall[p.first][p.second];
                        if(!inque[nx][ny])
                        {
                            update.push(make_pair(nx, ny));
                            inque[nx][ny] = true;                  
                        }                        
                    }
                    
                }
            }                                          
        }    
        
        /*
        for(int i = 1; i <= R; i++, printf("\n"))
            for(int j = 1; j <= C; j++)
                printf("%c", map[i][j]);
        */
        if(ans[cake.first][cake.second] == INT_MAX)
             printf("Case #%d: THE CAKE IS A LIE\n", z);
        else
             printf("Case #%d: %d\n", z, ans[cake.first][cake.second]);
    }
    return 0;   
}
