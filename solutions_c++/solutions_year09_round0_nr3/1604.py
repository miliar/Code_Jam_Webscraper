#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;
int r;
char a[40], we[] = "welcome to code jam";

bool bt(int x, int p)
{
	if (p == 19)
	{
		if (++r == 9999)
		{
			return true;
		}
		return false;
	}

	for (int i = x + 1; i < (int) strlen(a); i++)
	{
		if (a[i] == we[p])
		{
			if (bt (i, p + 1)) return true;
		}
	}

	return false;
}

int main(void)
{
	int n, t = 1;

	scanf("%d ", &n);

	while (n--)
	{
		r = 0;
		gets(a);
		
		for (int i = 0; i < (int) strlen(a); i++)
		{
			if (a[i] == 'w')
			{
				if (bt(i, 1)) break;
			}
		}

		printf("Case #%d: ", t++);
		if (r < 10)
		{
			printf("000%d", r);
		} else
			if (r < 100)
			{
				printf("00%d", r);
			}
			else
				if (r < 1000)
				{
					printf("0%d", r);
				}
				else
					printf("%d", r);
		printf("\n");
	}
	
	return 0;
}
