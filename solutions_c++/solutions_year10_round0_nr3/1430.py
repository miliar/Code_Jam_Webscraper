#include "stdafx.h"

#include <cstdio>
#include <cctype>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

int sum;
int groupSize[2000];
int indexToMoney[2000];
int indexToIndex[2000];
int history[2000];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int i, j, tc;
	scanf("%d",&tc);

	int r,k,n;
	for (i=0; i<tc; i++)
	{
		scanf("%d%d%d",&r,&k,&n);
		int totalGroups = 0;
		for (j=0; j<n; j++)
		{
			scanf("%d",&groupSize[j]);
			totalGroups+=groupSize[j];
		}



		if (totalGroups <= k)
		{
			printf("Case #%d: %d\n", i+1, r*totalGroups);
		}
		else
		{
			memset(history, 0, sizeof(history));
			int curr = 0;
			sum = 0;
			bool ending = false;
			while (r)
			{
				if (!ending)
				if (history[curr] == 1)
				{
					int cycleSum = 0;
					int untilCurr = curr;
					int cycles = 0;					
					do 
					{
						int innerSum = 0;
						while(1)
						{					
							if (innerSum + groupSize[untilCurr] > k)
								break;
							innerSum += groupSize[untilCurr];
							untilCurr = (untilCurr + 1) % n;							
						}
						cycles++;
						cycleSum += innerSum;
					} while (untilCurr != curr);

					if (cycles<=r)
					{
						sum += (r/cycles)*cycleSum;
						r = r% cycles;
					}

					ending = true;
				}
				
				if (!r) break;
				history[curr] = 1;
				int innersum = 0;
				while(1)
				{					
					if (innersum + groupSize[curr] > k)
						break;
					innersum += groupSize[curr];
					curr = (curr + 1) % n;
				}
				sum+=innersum;
				r--;
			}
			printf("Case #%d: %d\n", i+1, sum);
		}		
	}

	

	return 0;
}

