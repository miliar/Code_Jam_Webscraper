#include <cstdio>
#include <climits>
#include <cstring>
using namespace std;

int stocks[128][64];

bool adj[128][128];

int table[1 << 16][17];
int N, K;
int calc(int remain, int top)
{

    if(remain == 0)
        return 0;
    else if(table[remain][top])
        return table[remain][top] - 1;
    else
    {
        
        int v = INT_MAX;
        
        if(top != 0)
            v = 1 + calc(remain, 0);
            
        for(int i = 0; i < N; i++)
            if((remain & (1 << i)))
                if(!adj[i + 1][top] && stocks[top][0] < stocks[i + 1][0])
                {
                    int t = calc(remain & ~(1 << i), i + 1);      
                    if(v > t)
                        v = t;
                }
//                    printf("!%d %d %d\n", remain, top, v);
        return (table[remain][top] = v)++;
    }   
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; t++)
    {        
        scanf("%d%d", &N, &K);        
        for(int i = 1; i <= N; i++)
            for(int j = 0; j < K; j++)
                scanf("%d", &stocks[i][j]);
        
        for(int i = 0; i < K; i++)
            stocks[0][i] = -1;
      memset(table, 0, sizeof(table));          
        memset(adj, 0, sizeof(adj));
        for(int i = 1; i <= N; i++)
            for(int j = i + 1; j <= N; j++)
            {
                bool check = false;
                for(int k = 0; k < K; k++)        
                    if(stocks[i][k] == stocks[j][k])
                    {
                        check = true;
                        break;
                    }
                    
                if(!check)
                    for(int k = 0; k < K - 1; k++)        
                        if((stocks[i][k] < stocks[j][k]) != (stocks[i][k + 1] < stocks[j][k + 1]))
                        {
                            check = true;
                            break;                 
                        }
                if(check)
                {
//                         printf("#%d %d\n", i, j);
                    adj[i][j] = adj[j][i] = true;         
                }
            }
        
//        int a, b;
  //      while(scanf("%d%d", &a, &b) == 2)
    //        printf("%d\n", calc(a, b));
            
        printf("Case #%d: %d\n", t, 1 + calc((1 << N) - 1, 0));
    }
    return 0;   
}
