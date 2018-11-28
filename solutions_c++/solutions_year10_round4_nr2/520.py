#include<iostream>
#include<cstring>

using namespace std;

    int all[1000000], mas[1000000];
    long long sum[50][2000];
    long long dp[50][2000][50];
    int n;
 
   long long inf = 100000000000000000LL;

long long go(int red,int col, int have)
{
    if( red == n + 1 )
    {
     //printf("here for %d %d %d\n",red,col,have);
     if( have >= n- all[col] ) return 0;
     else return inf;
    }

    if( dp[red][col][have] != -1) return dp[red][col][have];

    dp[red][col][have] = inf;

    //printf("za %d %d %d imam %lld\n",red,col, have, sum[red][col]);
    dp[red][col][have] = min(dp[red][col][have],sum[red][col] + go(red+1,col*2,have+1) + go(red+1,col*2+1,have+1));
    dp[red][col][have] = min(dp[red][col][have], go(red+1,col*2,have) + go(red+1,col*2+1,have));

return dp[red][col][have];
}
void solve()
{
    scanf("%d", &n);
   
    for( int i = 0; i < (1<<n); ++i ) scanf("%d", &all[i]);

   //int u

    for( int j = n-1; j >= 0; --j )
     for( int i = 0; i < (1<<j); ++i ) {scanf("%lld", &sum[j+1][i]);/*printf("%d %d equals %lld\n",j+1,i,sum[j+1][i]);*/}

   memset(dp, -1, sizeof(dp));
   cout<<go(1,0,0)<<"\n";
    //printf("%lld\n",ans);
}
int main()
{
    int t;
    scanf("%d", &t);
   
    int ccc = 1;
    for(;t;t--)
     {
      printf("Case #%d: ",ccc); solve();
      ccc++;
    }
return 0;
}
