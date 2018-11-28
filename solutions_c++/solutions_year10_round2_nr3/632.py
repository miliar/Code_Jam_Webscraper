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

int dp[510][510];
int mod = 100003;
int C[510][510];
int max(int a,int b){return a>b?a:b;}
int solve(int n,int c)
{
	if(c==1)return 1;
	if(dp[n][c]!=-1)return dp[n][c];
	int &ret = dp[n][c];
	ret = 0;
	int num = n-c-1;
	for(int i=max(1,c-num-1);i<c;i++)
		ret+=((__int64)C[num][c-i-1]*solve(c,i))%mod;
	return ret;
}
int main()
{
	//freopen("C-small-attempt0.in","r",stdin);freopen("C-small-output.txt","w",stdout);
	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-output.txt","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large-output.txt","w",stdout);
	memset(dp,-1,sizeof(dp));
	int T;
	int i,j;
	memset(C,0,sizeof(C));
	for(i=0;i<510;i++)for(j=0;j<=i;j++)
		C[i][j]=((j==0)?1:((__int64)C[i-1][j-1]+C[i-1][j])%mod);
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		int n;
		scanf("%d",&n);
		__int64 ret = 0;
		for(i=1;i<n;i++)
			ret+=solve(n,i);
		printf("Case #%d: %d\n",Case,ret%mod);
	}
}