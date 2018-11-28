#include <cstdio>
#include <iostream>

using namespace std;

int main()
{	
	long long pd, pg, t, n;

	cin >> t;
	for (int i = 0; i < t; i++)
	{
		scanf("%I64d %I64d %I64d ", &n, &pd, &pg);
		bool ok = false;

		for (int j = 1; j <= n; j++)
		{
   			if ( j * pd % 100 == 0 )
   			{
   				ok = true;   		
   				break;
   		    }
   		}

		if ( (pg == 100 && pd != 100) || (pg == 0 && pd > 0) ) ok = false;

		printf("Case #%d: ", i + 1);
		if (!ok) 
			puts("Broken");
		else
			puts("Possible");
	}

	return 0;
}
