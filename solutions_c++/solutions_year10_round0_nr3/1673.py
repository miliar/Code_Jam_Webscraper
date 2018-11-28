#include <cstdio>
#include <vector>

using namespace std;

int T;

long long ps[1000];

long long R, k, N;

long long win_cache[1000];
int next_cache[1000];

int main(int argc, char** argv)
{
    scanf("%d", &T);
    
    for(int c = 1; c <= T; ++c)
    {
        scanf("%lld %lld %lld", &R, &k, &N);
        
        for(int i = 0; i < N; ++i)
            scanf("%lld", ps + i);
        
        for(int i = 0; i < N; ++i)
        {
            long long num_on = 0;
            long long num_available = k;
            int j = 0;
            
            for(j = 0; j < N; ++j)
            {
                int pos = (i+j)%N;
                
                if(ps[pos] > num_available)
                    break;
                
                num_on += ps[pos];
                num_available -= ps[pos];
            }
            
            win_cache[i] = num_on;
            next_cache[i] = (i+j)%N;
        }
        
        int pos = 0;
        long long ans = 0;
        
        for(int i = 0; i < R; ++i)
        {
            ans += win_cache[pos];
            pos = next_cache[pos];
        }
        
        printf("Case #%d: %lld\n", c, ans);
    }
    
    return 0;
}