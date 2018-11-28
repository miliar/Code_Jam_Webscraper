#include <cstdio>
#include <algorithm>

using namespace std;


bool grid[100][100][2];

int solve()
{
    int ans = 0;
    
    while(true)
    {
        bool this_gen = ans%2;
        bool last_gen = !this_gen;
        
        /*
        for(int j = 0; j < 10; ++j)
        {
            for(int k = 0; k < 10; ++k)
                printf("%d", grid[j][k][1]);
            
            printf("\n");
        }
        
        printf("\n\n");
        */
        
        for(int i = 0; i < 100; ++i)
        {
            for(int j = 0; j < 100; ++j)
            {
                if(grid[i][j][last_gen])
                {
                    if((j==0||!grid[i][j-1][last_gen]) && (i==0||!grid[i-1][j][last_gen]))
                        grid[i][j][this_gen] = false;
                    else
                        grid[i][j][this_gen] = true;
                }
                else
                {
                    if(i > 0 && j > 0 && grid[i][j-1][last_gen] && grid[i-1][j][last_gen])
                        grid[i][j][this_gen] = true;
                    else
                        grid[i][j][this_gen] = false;
                }
            }
        }
        
        bool clear = true;
        for(int i = 0; i < 100; ++i)
            for(int j = 0; j < 100; ++j)
                if(grid[i][j][last_gen])
                {
                    clear = false;
                    break;
                }
                
        if(clear)
            return ans;
        
        ++ans;
    }
}

int C;

int main(int argc, char** argv)
{
    scanf("%d", &C);
    
    for(int c = 1; c <= C; ++c)
    {
        for(int i = 0; i < 100; ++i)
            for(int j = 0; j < 100; ++j)
                grid[i][j][0] = grid[i][j][1] = false;
            
        int num_rects;
        scanf("%d", &num_rects);
        
        for(int i = 0; i < num_rects; ++i)
        {
            int x1, x2, y1, y2;
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            
            for(int j = x1 - 1; j < x2; ++j)
                for(int k = y1 - 1; k < y2; ++k)
                    grid[j][k][1] = true;
        }
        

        printf("Case #%d: %d\n", c, solve());
    }
}