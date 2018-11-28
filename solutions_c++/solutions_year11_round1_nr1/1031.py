#include <iostream>
#include <queue>
#include <vector>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

#define first A
#define second B

int main()
{
	long long l, N, pd, pg;
	int i, k, T;
	cin >> T;
	for (k=1; k<=T; ++k)
	{
		l = 100;
		cin >> N >> pd >> pg;
		if (((pd < 100) && (pg == 100)) || ((pd > 0) && (pg == 0)))
			printf("Case #%d: Broken\n",k);
		else
		{
			for (i=2; i<=pd; ++i)
			{
				while ((pd % i == 0) && (l % i == 0))
				{
					l /= i;
					pd /= i;
				}
			}
			if (pd == 0)
				printf("Case #%d: Possible\n",k);
			else if (N < l)
				printf("Case #%d: Broken\n",k);
			else
				printf("Case #%d: Possible\n",k);
		}
	}
	return 0;
}
