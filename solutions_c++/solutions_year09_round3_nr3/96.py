#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

    int len, n;
    int mas[10000];

    int dp[200][200];

    int Right[200], Left[200];

int go(int x,int y)
{
    if(x>y)return 0;
    if(dp[x][y]!=-1)return dp[x][y];
    
    dp[x][y] = 2000000000;

    int i;
    for( i = x; i <= y; ++i )
    dp[x][y] = min(dp[x][y], go(x,i-1) + go(i+1, y) + Right[y] - Left[x]);

return dp[x][y];
}
void solve()
{
   scanf("%d%d",&len,&n);
   
   int i;

   for( i = 0; i < n; ++i)scanf("%d", &mas[i]);
   sort(mas, mas + n);

   for( i = 0; i < n; ++i )
   {
    if(i!=0)Left[i] = mas[i-1] + 1;
    else Left[0] = 1;

    if(i!=n-1)Right[i] = mas[i+1] - 1;
    else Right[i] = len;
   }
   
   memset(dp, -1, sizeof(dp));

   printf("%d\n",go(0,n-1));   
}
int main()
{
   int t;
   scanf("%d", &t);
 
   for(int i = 1; i <= t; ++i)
   {
    printf("Case #%d: ",i);
    solve();
   }
return 0;
}
