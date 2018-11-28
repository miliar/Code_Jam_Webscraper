#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int nbTest;

int
main()
{
	scanf("%d", &nbTest);
	
	for(int test = 1; test <= nbTest; test++)
	{
		int N, pd, pg;
		scanf("%d%d%d", &N, &pd, &pg);
		
		
		if(pg == 100 && pd < 100)
		{
			printf("Case #%d: Broken\n", test);
			continue;
		}
		if(pg == 0 && pd > 0)
		{
			printf("Case #%d: Broken\n", test);
			continue;
		}
		
		else
		{
			bool affiche = false;
			
			for(int partie = 1; partie <= min(100, N); partie++)
			{
				if(((partie * pd) % 100) == 0)
				{
					printf("Case #%d: Possible\n", test);
					affiche = true;
					break;
				}
			}
			
			if(!affiche)
				printf("Case #%d: Broken\n", test);
		}
	}
	

	return 0;
}

