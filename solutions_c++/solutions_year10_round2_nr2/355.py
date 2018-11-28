#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

class Rational
{
    public:
    long long den, num;
    
    Rational(long long _ = 0, long long __ = 1)
    {
        num = _;
        den = __;
    }
    
    bool operator<(const Rational& r) const
    {
        long long lhs = num*r.den;
        long long rhs = r.num*den;
        
        return lhs < rhs;
    }
    
    bool check(long long t)
    {
        return num <= den*t;
    }
};

long long N, K, B, T;

long long pi[51];
long long vi[51];

pair<Rational, int> times[51];
pair<long long, Rational> poses[51];
int slow_ahead[51];

int main(int argc, char** argv)
{
    int C;
    scanf("%d", &C);
    
    for(int c = 1; c <= C; ++c)
    {
        
        scanf("%lld %lld %lld %lld", &N, &K, &B, &T);
        
        for(int i = 0; i < N; ++i)
            scanf("%lld", pi+i);
        
        for(int i = 0; i < N; ++i)
            scanf("%lld", vi+i);
        
        for(int i = 0; i < N; ++i)
            times[i] = make_pair(Rational(B - pi[i], vi[i]), -i);
        
        sort(times, times + N);
        
        for(int i = 0; i < N; ++i)
            poses[i] = make_pair(B - pi[i], Rational(B - pi[i], vi[i]));
        
//         sort(poses, poses+N);
        
        for(int i = 0; i < N; ++i)
        {
            slow_ahead[i] = 0;
            for(int j = 1; j < N; ++j)
                slow_ahead[i] += !poses[j].second.check(T);
            
//             printf("%d %d\n", i, slow_ahead[i]);
        }
        
        long long best = 0;
        
        for(int i = 0; i < N; ++i)
        {
            best += times[i].first.check(T);
//             printf("%lld/%lld %d Check = %d\n", times[i].first.num, times[i].first.den, times[i].second, times[i].first.check(T));
        }
        
//         printf("%lld %lld\n", best, K);
        
//         printf("\n");
        
        if(best < K)
        {
            printf("Case #%d: IMPOSSIBLE\n", c);
        }
        else
        {
            long long num_ahead = 0;
            
            long long saved = 0;
            
            long long ans = 0;
            
            for(int i = N-1; i >= 0; --i)
            {
                if(saved == K)
                    break;
                
                if(!poses[i].second.check(T))
                {
                    ++num_ahead;
                }
                else
                {
                    ans += num_ahead;
                    ++saved;
                }
            }
            
            printf("Case #%d: %lld\n", c, ans);
        }
        

    }
    return 0;
}