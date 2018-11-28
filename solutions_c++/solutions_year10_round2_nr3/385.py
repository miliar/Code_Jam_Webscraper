#include<iostream>
#include<algorithm>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
#include<cmath>
#include<queue>
#define mp make_pair
#define ll long long

using namespace std;
 
    int ans = 0;
    int n;
    
    const int mod = 100003;
    
    int dp[501][501][501];
    
int go(int pos,int need, int last)
{
   // printf("%d %d %d\n", pos, need, last);
    //system("pause");
    if(need < 0)return 0;
    if( pos == 1 )
    {
     if(need == 0 && last == 1)return 1;
     else return 0;
    }
    if(dp[pos][need][last] != -1)return dp[pos][need][last];
    
    dp[pos][need][last] = 0;
    
    if(pos == last){
           dp[pos][need][last] += go(pos-1, need - 1, need);
           dp[pos][need][last] %= mod;
    }
    else
    {
         dp[pos][need][last] += go(pos-1, need, last);          dp[pos][need][last] %= mod;
         dp[pos][need][last] += go(pos-1, need - 1, last); dp[pos][need][last] %= mod;
    }
    //cout<<" za "<<pos<<" "<<need<<" "<<last<<" "<<dp[pos][need][last]<<"\n";
return dp[pos][need][last];
}
void solve()
{
     cin>>n;
     
     
     ans = 0;
     for( int i = 1; i < n; ++i )
      {ans += go(n-1,i-1,i); ans %= mod;}
      
     printf("%d\n", ans);
}
int main()
{
    int t;
    scanf("%d", &t);
    memset(dp, -1, sizeof(dp));
    for( int i = 1; i <= t; ++i ) 
    {
         printf("Case #%d: ", i);
         solve();
     }
return 0;
}
