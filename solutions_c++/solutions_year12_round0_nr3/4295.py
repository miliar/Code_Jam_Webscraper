#include <stdio.h>
#include <set>
#include <algorithm>

int main(int, char **)
{
	int numCases;

	scanf("%d", &numCases);
	char strN[128];

	for(int i = 0;i < numCases; ++i)
	{		
		int a,b;
		scanf("%d %d", &a, &b);

		int num = 0;
		for(int m = a +1; m <= b; ++m)
		{			
			for(int n = a;n < m; ++n)
			{				
				int lenStrN = sprintf(strN, "%d", n);

				for(int tries = 0;tries < lenStrN; ++tries)
				{
					std::rotate(&strN[0], &strN[lenStrN-1], &strN[lenStrN]);

					int newNumber;
					sscanf(strN, "%d", &newNumber);

					if(newNumber == m)
					{
						++num;
						break;
					}
				}
			}
		}

		printf("Case #%d: %d\n", i+1, num);		
	}
}