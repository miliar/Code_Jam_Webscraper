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

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n ;
	scanf("%d",&n);
	int i;
	char tt[50];
	int dp[50];
	for(i=1;i<=n;i++)
	{
		int r;
		scanf("%d",&r);
		memset(dp,0,sizeof(dp));
		int tmp =r;
		int j;
		for(tmp = 0;tmp<r;tmp++)
		{

			scanf("%s",tt);
			
			
			int count=0;
			for(j=0;j<strlen(tt);j++)
				if(tt[j]=='1')
					count = j;
			dp[tmp]=count;
		}
		int ret =0;
		for(j=0;j<r;j++)
		{
			if(dp[j]>j)
			{
				for(int k =j+1;k<r;k++)
					if(dp[k]<=j)
					{
						ret+=k-j;
						int tt = dp[k];
						for(int t=k;t>j;t--)
							dp[t] = dp[t-1];
						dp[j]=tt;
						break;
					}
			}
		}
		printf("Case #%d: %d\n",i,ret);
	}
}