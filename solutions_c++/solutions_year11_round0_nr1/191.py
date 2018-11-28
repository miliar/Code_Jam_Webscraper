#include <stdio.h>
#include <stdlib.h>
#define max(a,b) (a>?b)

int main()
{
	int t, n, p;
	int posO, posB, timeO, timeB;
	char r[2];
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		posO = posB = 1;
		timeO = timeB = 0;
		scanf("%d", &n);
		for (int j=0;j<n;j++)
		{
			scanf("%s%d", &r[0], &p);
			if (r[0]=='O')
			{
				timeO += abs(posO-p);
				posO = p;
				timeO = max(timeO, timeB)+1;
			}
			else if (r[0]=='B')
			{
				timeB += abs(posB-p);
				posB = p;
				timeB = max(timeO, timeB)+1;
			}
		}
		printf("Case #%d: %d\n", i, max(timeO, timeB));
	}
	return 0;
}
