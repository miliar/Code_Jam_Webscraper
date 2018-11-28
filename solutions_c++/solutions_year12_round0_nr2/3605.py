#include <stdio.h>

int main()
{
	int t, n, p, s, v, i, j;
	int count;
	
	scanf("%d",&t);
	getchar();
	fflush(stdin);
	
	for(i=0; i<t; i++)
	{
		scanf("%d %d %d", &n, &s, &p);
		count = 0;
		for(j=0; j<n; j++)
		{
			scanf("%d", &v);
			if ((v+2)/3 >= p)
				count++;
			else if ((v+4)/3 >= p && s && v) 
			{
				count++;
				s--;
			}
		}
		printf("Case #%d: %d\n", i+1, count);
	}
	
	return 0;
}	
