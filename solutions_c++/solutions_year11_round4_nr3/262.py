#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

const int MAXN = 1000100;
bool notp[MAXN];
vector <long long> primes;

void sieve()
{
    notp[0] = notp[1] = true;
    for(int i = 0; i < MAXN; i++)
        if(!notp[i])
        {
            primes.push_back(i);
            for(int j = i*2; j < MAXN; j+=i)
                notp[j] = true;
        }
}

int main()
{
    sieve();
    freopen("cin.in", "r", stdin);
    freopen("outc_l.txt", "w", stdout);
    int T;
    long long N;
    cin>>T;
    
    for(int t = 1; T--; ++t)
    {
        cin>>N;
        long long a = 0, b = 0;
        for(int i = 0; primes[i] <= N && i < primes.size(); i++)
        {
            long long vv = primes[i], tempv = N;
            ++a;
            while(tempv>=primes[i])
            {
                ++b;
                tempv /= vv;
            }
        }
        
        if(N!=1) b++;
        cout<<"Case #"<<t<<": "<<b-a<<endl;
    }
    
    return 0;
}
