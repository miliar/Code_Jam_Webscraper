/*
    2011 Round 2 -
    Expensive Dinner
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std ;

    int T;
    long long N;
    long long ans;

    bool isnt_prime[1000000];
    vector<int> prime;

int main() {
    for(int i=2; i<1000000; ++i)
    {
        if(!isnt_prime[i])
        {
            prime.push_back(i);
            for(int j=i+i; j<1000000; j+=i)
                isnt_prime[j] = true;
        }
    }
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        scanf("%I64d", &N);
        ans = 0;
        if(N==1)
        {
            ans = 0;
        }
        else
        {
            for(int i=0, maxi=prime.size(); i<maxi; ++i)
            {
                long long p = prime[i];
                if(p*p>N) break;
                long long tN = N/p;
                while(tN>=p)
                {
                    tN/=p;
                    ++ans;
                }
            }
            ++ans;
        }
        printf("Case #%d: %I64d\n", z, ans);
    }
    return 0;
}
