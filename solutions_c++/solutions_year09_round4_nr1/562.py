#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; t++)
    {
        int N;
        scanf("%d", &N);
        
        int rows[64] = {0};
        
        for(int i = 0; i < N; i++)
        {
            char c;
            for(int j = 0; j < N; j++)
            {
                scanf(" %c", &c);
                if(c == '1')
                    rows[i] = j + 1;
            }                
            
            
        }
        
        int ans = 0;
        for(int i = 0; i < N; i++)
        {
            for(int j = i; j < N; j++)
            {
                if(rows[j] <= i + 1)
                {
                          
                    for(int k = j - 1; k >= i; k--)
                        swap(rows[k], rows[k + 1]), ans++;
                        
                    break;
                }
            }                
        }        
        printf("Case #%d: %d\n", t, ans);                
            
    }
    
    return 0;   
}
