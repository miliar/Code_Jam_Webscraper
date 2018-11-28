#include <cstdio>
using namespace std;




int main()
{
    int N;
    scanf("%d", &N);
    for(int z=  1; z <= N; z++)
    {
        int H, W, R;
        scanf("%d%d%d", &H, &W, &R);
        
        int table[128][128] = {0};
        bool rock[128][128] = {0};
        
        while(R--)
        {
            int r, c;
            scanf("%d%d", &r, &c);
            rock[r - 1][c - 1] = true;          
        }
        
        table[0][0] = 1;
        for(int i = 0; i < H; i++)
            for(int j = 0; j < W; j++)
                if(!rock[i][j])
                {
                    table[i + 2][j + 1] += table[i][j];
                    table[i + 2][j + 1] %= 10007;
                    table[i + 1][j + 2] += table[i][j];
                    table[i + 1][j + 2] %= 10007;      
                }
        
        
        
        printf("Case #%d: %d\n", z, (rock[H - 1][W - 1]? 0: table[H - 1][W - 1]));
            
    }
    return 0;   
}
