#include <cstdio>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
    int C;
    scanf("%d", &C);
    
    for(int c = 1; c <= C; ++c)
    {
        vector<long long> freqs;
        
        int N;
        long long L, H;
        scanf("%d %lld %lld", &N, &L, &H);
        
        for(int i = 0; i < N; ++i)
        {
            long long l;
            scanf("%lld", &l);
            freqs.push_back(l);
        }
        
        long long maxi = freqs[0];
        
        /**
        for(int i = 0; i < N; ++i)
            maxi = max(maxi, freqs[i]);
        
        vector<long long> primes;
        while(maxi % 2 == 0)
        {
            maxi /= 2;
            primes.push_back(2);
        }
        
        while(maxi != 1)
        {
            for(long long  i = 3; i*i < maxi; i += 2)
            {
                while(maxi % i == 0)
                {
                    primes.push_back(i);
                    maxi /= i;
                }
            }
        }
        **/
        
        long long ans = -1;
        for(long long b = L; b <= H; ++b)
        {
            bool can_do = true;
            
            for(int i = 0; i < N; ++i)
            {
                if(!(freqs[i] % b == 0 || b % freqs[i] == 0))
                {
                    can_do = false;
                    break;
                }
            }
            
            if(can_do)
            {
                ans = b;
                break;
            }
        }
        
        if(ans != -1)
            printf("Case #%d: %lld\n", c, ans);
        else
            printf("Case #%d: NO\n", c);
    }
    return 0;
}