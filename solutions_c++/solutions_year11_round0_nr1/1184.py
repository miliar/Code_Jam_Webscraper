#include "stdio.h"
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
	freopen("F:\\code\\topcoder\\A-large.in","r",stdin);
	freopen("F:\\code\\topcoder\\result.txt","w",stdout);
	int caseNum = 0;
	int t,n;
	int lastOTime = 0,lastBTime = 0;
	int lastOAddr = 1,lastBAddr = 1;
	int costTime = 0;
	scanf("%d",&t);
	while (caseNum < t)
	{
		lastOAddr = lastBAddr = 1;
		lastOTime = lastBTime = 0;
		costTime = 0;
		scanf("%d",&n);
		for (int i = 0;i<n;i++)
		{
			char c;
			int addr;
			while((c = getchar())!='O' && c != 'B');
			scanf("%d",&addr);
			if (c == 'O')
			{
				costTime = max(costTime+1,lastOTime+abs(addr-lastOAddr)+1);
				lastOTime = costTime;
				lastOAddr = addr;
			}
			else
			{
				costTime = max(costTime+1,lastBTime+abs(addr-lastBAddr)+1);
				lastBTime = costTime;
				lastBAddr = addr;
			}
		}
		printf("Case #%d: %d\n",caseNum+1,costTime);
		caseNum++;
	}
}