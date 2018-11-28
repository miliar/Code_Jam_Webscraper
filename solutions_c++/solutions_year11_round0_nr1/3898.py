#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

char c, c1;
int n, i, maxO, maxB, pozO, pozB, t, d, k, x;

int main()
{
	freopen("bottrust.in" , "r" , stdin);
	freopen("bottrust.out", "w" , stdout);
	
	scanf("%d\n" , &t);
	for(k = 1 ; k <= t ; ++k)
	{
		scanf("%d ", &n);
		maxO = maxB = 0;
		pozO = pozB = 1;
		for(i = 1 ; i <= n ; ++i)
		{
			scanf("%c %d ", &c, &x);
			if(i==1 && c == 'O')
			{
				maxO = maxO + (x-pozO)+1;
				pozO = x;
			}
			else
				if(i==1)
				{
					maxB = maxB + (x-pozB)+1;
					pozB = x;
				}
			else
			{
				if(c=='O')
					d = abs(x-pozO) + 1;
				else
					d = abs(x-pozB) + 1;
				if(c==c1 && c1 == 'O')
				{
					maxO = maxO+d;
					pozO = x;
				}
				else
					if(c==c1 && c1 == 'B')
					{
						maxB = maxB+d;
						pozB = x;
					}
				else
					if(c=='O')
					{
						maxO = max(maxO+d,maxB+1);
						pozO = x;
					}
					else
					{
						maxB = max(maxB+d,maxO+1);
						pozB = x;
					}
			}
			c1=c;
		}
		printf("Case #%d: ", k);
		if(maxO > maxB)
			printf("%d\n", maxO);
		else
			printf("%d\n", maxB);
	}
	return 0;
}




