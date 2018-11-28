#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

long long t, tt;
long long n, m, x, y, z;
long long A[500005], S[500005];
long long dp[500005];

void input()
{
     scanf("%lld %lld %lld %lld %lld", &n, &m, &x, &y, &z);

     for (int i = 0; i < m; i++) { scanf("%lld", &A[i]);} 
     for (int i = 0; i < n; i++)
     {
         S[i] = A[i % m];
         //cout << S[i] << " ";
         A[i % m] = (x * A[i % m] + y * (i + 1)) % z;
     }    
}  

void solve()
{
    for (int i = 0; i < n; i++) dp[i] = 1;
    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (S[j] < S[i]) dp[i] += dp[j] % (long long)1000000007;
        }    
    }  
    long long ans = 0;
    for (int i = 0; i < n; i++) 
    {
        ans += dp[i];
        //cout << dp[i] << endl;
    }    
    cout << "Case #" << ++tt << ": " << ans % (long long)1000000007 << endl;
}    

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    //freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%lld", &t);
    while (t--)
    {
        input();
        solve();
    }  
}    
