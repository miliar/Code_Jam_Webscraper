#include <cstdio>
#include <cstring>
using namespace std;


struct
{
    int x, y;      
}dif[]=
{
    -1, 0,
     0,-1,
     0, 1,
     1, 0       
};

unsigned int hmap[128][128];
char label[128][128];
char now;

char draw(int x, int y)
{
    if(!label[x][y])
    {         
        char ret = 0;
        
        int fx = -1, fy = -1;
        for(int d = 0; d < 4; d++)
        {
            int dx = x + dif[d].x;
            int dy = y + dif[d].y;
            
            if(hmap[dx][dy] < hmap[x][y] && (fx == -1 || hmap[fx][fy] > hmap[dx][dy]))
            {
                fx = dx;
                fy = dy;
            }
        }
        
        if(fx == -1)            
            label[x][y] = now++;
        else
            label[x][y] = draw(fx, fy);
    }
            
    return label[x][y];     
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; t++)
    {
        int H, W;
        scanf("%d%d", &H, &W);
        
        memset(hmap, -1, sizeof(hmap));
        memset(label, 0, sizeof(label));
        for(int i = 1; i <= H; i++)
            for(int j = 1; j <= W; j++)
                scanf("%u", &hmap[i][j]);
         
        now = 'a';       
        for(int i = 1; i <= H; i++)
            for(int j = 1; j <= W; j++)
                if(!label[i][j])
                    draw(i, j);    
            
        printf("Case #%d:\n", t);
        for(int i = 1; i <= H; i++, printf("\n"))
            for(int j = 1; j <= W; j++)
            {
                if(j > 1)
                    printf(" ");      
                printf("%c", label[i][j]);
            }
    }
    return 0;   
}
