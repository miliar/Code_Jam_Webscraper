#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

#include<vector>
#include<iostream>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include"bigint.h"

using namespace std;

BigInt gcd(BigInt a, BigInt b)
{
    if(b == "0") return a;
    return gcd(b,a%b);   
}

bool comp(const BigInt &x, const BigInt &y)
{
    if(x.size != y.size) return x.size < y.size;
    for(int i = 0; i < x.size; ++i)
    {
        if(x.digits[i] != y.digits[i])
        return x.digits[i] < y.digits[i];   
    } 
    return false;
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    
    int T; scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        int N; scanf("%d",&N);
        
        vector<BigInt> tm;
        
        for(int i = 0; i < N; ++i)
        {
            string s; cin >> s;
            tm.push_back(BigInt(s));   
        }
        
        sort(tm.begin(),tm.end(),comp);
        
        BigInt g = tm[1]-tm[0];
        
        for(int i = 2; i < N; ++i)
        {
            g = gcd(g,tm[i]-tm[i-1]);   
        }
        
        BigInt rem = tm[0]%g;
        
        BigInt ans = g-rem;
        
        ans = ans%g;
        
        printf("Case #%d: ",t);
        
        cout << ans << endl;
    }
    
    return 0;
}
