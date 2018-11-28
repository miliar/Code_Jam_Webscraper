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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int T,N;
typedef long long LL;
const int MAX=10000;
LL dp[MAX];
LL D[MAX],L[MAX];
LL len;

void init()
{
	for(int i=0;i<N;i++)
		scanf("%lld%lld",D+i,L+i);
	scanf("%lld",&len);
}
queue<int> Q;
bool work()
{
	int a;
	memset(dp,0,sizeof(dp));
	dp[0]=D[0];
	while(!Q.empty())
		Q.pop();
	Q.push(0);
	while(!Q.empty())
	{
		a=Q.front();
		Q.pop();
		for(int b=a+1;b<N && D[b]-D[a]<=dp[a];b++)
		{
			LL x=min(D[b]-D[a],L[b]);
			if(x>dp[b])
			{
				dp[b]=x;
				Q.push(b);
			}
		}
	}
	bool suc=false;
	for(int i=0;i<N;i++)
	{
		if(dp[i]+D[i]>=len)
		{
			suc=true;
			break;
		}
	}
	return suc;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int cnb=1;cnb<=T;cnb++)
	{
		scanf("%d",&N);
		init();
		bool res=work();
		printf("Case #%d: %s\n",cnb,res?"YES":"NO");
	}
}