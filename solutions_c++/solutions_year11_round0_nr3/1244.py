#include <cstdio>
#include <utility>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int N;
int items[1001];

int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        
        scanf("%d", &N);
        for(int i = 0; i < N; ++i)
            scanf("%d", items + i);
        
        int ans = -1;
        
        int lim = (1 << N);
        for(int i = 1; i < lim - 1; ++i)
        {
            
            int sean_sum = 0;
            int sean_xor = 0;
            
            int pat_sum = 0;
            int pat_xor = 0;
            
            int assignment = i;
            int item_num = 0;
            
            for(int _ = 0; _ < N; ++_)
            {                
                if(assignment % 2 == 0)
                {
                    /// Goes to sean
                    sean_sum += items[item_num];
                    sean_xor ^= items[item_num];
                }
                else
                {
                    /// Goes to patrick
                    pat_sum += items[item_num];
                    pat_xor ^= items[item_num];
                }
                
                ++item_num;
                assignment /= 2;
            }
            
            if(sean_xor == pat_xor)
                if(sean_sum > ans)
                    ans = sean_sum;
        }
        
        if(ans == -1)
            printf("NO\n");
        else
            printf("%d\n", ans);
    }
    
    return 0;
}