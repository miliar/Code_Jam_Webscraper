// May 20, 2011
// Author :: MIB


#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>


using namespace std;


int main(void)
{
	freopen ("C:\\codejam\\input\\A-large.in", "rt", stdin);
	freopen ("C:\\codejam\\output\\A-large.out", "wt", stdout);

	int i, j, t;
	__int64 n, d, g;
	char str[10];

	while(1 == scanf(" %d",&t))
	{
		for(i=1; i<=t; i++)
		{
			strcpy(str, "Broken");
			scanf(" %I64d %I64d %I64d" ,&n ,&d ,&g);

			if(g == 0)
			{
				if(d == 0)
					strcpy(str, "Possible");
				else
					strcpy(str, "Broken");
			}

			else if(g == 100)
			{
				if(d == 100)
					strcpy(str, "Possible");
				else
					strcpy(str, "Broken");
			}

			else {

				for(j=100; j>0; j--)
				{
					if(d % j == 0 && 100 % j == 0)
						break;
				}

				int k = 100 / j;
				if(k > n)
					strcpy(str, "Broken");
				else
					strcpy(str, "Possible");
			}
			
			printf( "Case #%d: %s\n" ,i ,str);
		}
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
