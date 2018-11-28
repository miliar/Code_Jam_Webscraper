#include <cstdio>

char mapping[100];

int dp[101][101];

int H, W;

int dw[] = {0, -1, 1, 0};
int dh[] = {-1, 0, 0, 1};

int basins[101][101];

int num_sinks = 0;


int recurse(int h, int w)
{
    if(dp[h][w] != -1)
        return dp[h][w];
    
    int lowest = -1;
    
    for(int i = 0; i < 4; ++i)
    {
        int nh = h + dh[i];
        int nw = w + dw[i];
        
        if(nh >= 0 && nh < H && nw >= 0 && nw < W)
        {
            if(lowest == -1)
            {
                lowest = i;
            }
            else
            {
                int oh = h + dh[lowest];
                int ow = w + dw[lowest];
                
                if(basins[nh][nw] < basins[oh][ow])
                    lowest = i;
            }
        }
    }
    
    int ph = h + dh[lowest];
    int pw = w + dw[lowest];
    
    if(basins[h][w] <= basins[ph][pw])
    {
        /// Sink
        dp[h][w] = num_sinks++;
    }
    else
    {
        dp[h][w] = recurse(ph, pw);
    }
    
    return dp[h][w];
}

int main()
{
    int T;
    
    scanf("%d", &T);
    
    for(int c = 1; c <= T; ++c)
    {
        num_sinks = 0;
        
        printf("Case #%d:\n", c);
        scanf("%d %d", &H, &W);
        
        for(int i = 0; i < H; ++i)
            for(int j = 0; j < W; ++j)
                dp[i][j] = -1;
            
        for(int i = 0; i < H; ++i)
            for(int j = 0; j < W; ++j)
                scanf("%d", basins[i]+j);
            
        for(int i = 0; i < H; ++i)
            for(int j = 0; j < W; ++j)
                recurse(i, j);
        
        for(int i = 0; i < 26; ++i)
            mapping[i] = 0;
        
        char next_mapping = 'a';
        
        for(int i = 0; i < H; ++i)
        {
            for(int j = 0; j < W; ++j)
            {
                if(mapping[dp[i][j]] == 0)
                    mapping[dp[i][j]] = next_mapping++;
                
                printf("%c", mapping[dp[i][j]]);
                
                if(j != W-1)
                    printf(" ");
            }
            
            printf("\n");
        }   
            
    }
}