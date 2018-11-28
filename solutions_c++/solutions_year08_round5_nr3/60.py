#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int table[32][2048];
int rooms[32] =  {0};
int N, M;

int calc(int x, int mask)
{
    //printf("%d %d\n", x, y);
    if(x >= N)
        return 0;
    else if(table[x][mask] > 0)
        return table[x][mask] - 1;
    else
    {
        int &v = table[x][mask];
        
        v = 0;
        
        for(int z = (1 << M) - 1; z >= 0; z--)
            if(!(z & rooms[x]))
            {
                bool flag = true;
                int c = 0;
                for(int y = 0; y < M; y++)
                    if((z & (1 << y)))
                    {
                        if(y && (z & (1 << (y - 1))))
                        {
                            flag = false;
                            break;     
                        }
                        c++;
                        if((y && (mask & (1 << (y - 1)))) || (y != M - 1 && (mask & (1 << (y + 1)))))
                        {
                            flag = false;
                            break;
                        }
                    }
                if(flag)
                    v = max(v, c + calc(x + 1, z));
            }
        v++;        
        return v - 1;
    }     
}

int main()
{
    int C;
    scanf("%d", &C);
    
    for(int z = 1; z <= C; z++)
    {

        
        memset(rooms, 0, sizeof(rooms));
        memset(table, 0, sizeof(table));
        
        scanf("%d%d", &N, &M);
        char buf[32];
        fgets(buf, 32, stdin);
        for(int i = 0; i < N; i++)
        {
            fgets(buf, 32, stdin);
            for(int j = 0; j < M; j++)
                if(buf[j] == 'x')
                    rooms[i] |= (1 << j);                      
        }        
        
        printf("Case #%d: %d\n", z, calc(0, 0));

            
    }
    return 0;   
}
