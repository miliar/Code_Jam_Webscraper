#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;
int dp[505][505],C[505][505];
int ans[505];
int GetAns(int a,int b)
{
	if(b>a-1)return 0;
	if(b==a-1)return 1;
	if(b==1)return 1;
	int& ret = dp[a][b];
	if(ret>=0)return ret;
	ret=0;
	for(int i=1;i<=b-1;i++)
	{
		ret=(ret+GetAns(b,i)*C[a-b-1][b-i-1])%100003;
	}
	return ret;
}
void init()
{
	C[1][0]=C[1][1]=1;
	for(int i=2;i<=500;i++)
	{
		C[i][0]=C[i][i]=1;
		for(int j=1;j<=i;j++)
			C[i][j]=(C[i-1][j]+C[i-1][j-1])%100003;
	}
	memset(ans,0,sizeof(ans));
	memset(dp,-1,sizeof(dp));
	for(int i=1;i<=500;i++)
		for(int j=1;j<i;j++)
			ans[i]=(ans[i]+GetAns(i,j))%100003;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	init();
	for(int cas=1;cas<=cases;cas++)
	{
		int N;
		scanf("%d",&N);
		printf("Case #%d: %d\n",cas,ans[N]);
		
	}
}
