#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 
using namespace std;
typedef long long ll;

const int mod = 10000;
int dp[520][20];
int n,m;
char str[520];
char wel[] = "welcome to code jam";
int go(int pos, int now)
{
	if(now == 0) 
		return dp[pos][now] = 1;
	if(pos == 0) 
		return dp[pos][now] = 0;
	if(dp[pos][now] >= 0) 
		return dp[pos][now];
	int res = 0;
	if(str[pos - 1] == wel[now - 1])
		res = (res + go(pos - 1, now - 1)) % mod;
	res = (res + go(pos - 1, now)) % mod;
	return dp[pos][now] = res;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
    scanf("%d", &n);
	getchar();
	for(int i = 0; i < n; i++)
	{
		gets(str);
        m = strlen(str);
		memset(dp, 0xff, sizeof dp);
		printf("Case #%d: %04d\n", i + 1, go(m, 19));
	}	
}
