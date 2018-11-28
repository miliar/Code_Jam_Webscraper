#include <memory>
#include <cstdio>
#include <iostream>
int dp[510][20], no = 1;
char word[510];
char str[20] = "welcome to code jam";
using namespace std;
int main()
{
freopen("f://C-small-attempt0.in", "r", stdin);
freopen("f://C-small-attempt0.out", "w", stdout);
int t;
scanf("%d", &t);
gets(word);
while( t-- )
{
gets(word);
int len = strlen(word), i, j;
memset(dp, 0, sizeof(dp));
int sum = 0;
for(i=0; i<len; ++i)
{
if( word[i] == 'w' ) dp[i][0] =  ++sum;
else dp[i][0] = sum;
}
for(i=1; i<len; ++i)
{
for(j=1; j<19; ++j)
{
if( word[i] == str[j] ) dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
else dp[i][j] = dp[i-1][j];
dp[i][j] %= 10000;
}
}
printf("Case #%d: %04d\n", no++, dp[len-1][18]);
}
return 0;
}