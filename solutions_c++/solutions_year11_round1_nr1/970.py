#include <cstdio>
#include <vector>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

int main()
{
	int Q;
	scanf("%d", &Q);
	
	for (int q = 1; q <= Q; ++q)
	{
		printf("Case #%d: ", q);
		
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		bool good = false;
		
		int i = 1;
		for (; i <= a; ++i)
		{
			if ((i*b)%100 == 0)
			{
				good = true;
				break;
			}
		}
		if (!good)
		{
			printf("Broken\n");
			continue;
		}
		if ((c == 100 && b != 100) || (b != 0 && c == 0))
		{
			printf("Broken\n");
			continue;
		}
		printf("Possible\n");
	}
	
	return 0;
}

