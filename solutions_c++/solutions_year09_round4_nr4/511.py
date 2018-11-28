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

double esp = 1e-8;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int C;
	scanf("%d",&C);
	int dp[50][3];
	bool v[50];
	for(int times=1;times<=C;times++)
	{
		int n;
		int i,j;
		scanf("%d",&n);
		memset(dp,0,sizeof(dp));
		for(i=0;i<n;i++)
			scanf("%d %d %d",&dp[i][0],&dp[i][1],&dp[i][2]);
		double ret = 0.0;
		double mid,l=0.0,h=1000;
		if(n<=2)
		{
			ret = dp[0][2];
			if(n==2)
				ret = dp[1][2]>dp[0][2]?dp[1][2]:dp[0][2];
			printf("Case #%d: %f\n",times,ret);
			continue;
		}
		
		while(h-l>esp)
		{
			mid = (l+h)/2;
			int count = 0;
			memset(v,false,sizeof(v));
			for(i=0;i<n;i++)
			{
				if(!v[i])
				{
					v[i] = true;
					count++;
					for(j=i+1;j<n;j++)
					{
						double len = dp[i][2]+dp[j][2];
						len += sqrt((dp[i][0]-dp[j][0])*(dp[i][0]-dp[j][0])+(dp[i][1]-dp[j][1])*(dp[i][1]-dp[j][1]));
						if(len - 2*mid<esp)
							v[j]=true;
					}
				}
				if(count>2)
					break;
			}
			if(count>2)
				l = mid;
			else
			{
				ret = mid;
				h = mid;
			}
		}
		printf("Case #%d: %f\n",times,ret);
	}
}