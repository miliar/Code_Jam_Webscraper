#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	int T,t;
	scanf("%d", &T);
	for(t = 1;t <= T; t++)
	{
		int N,S,p;
		scanf("%d%d%d", &N, &S, &p);
		int ans = 0;
		for(int i= 0; i< N; i++)
		{
			int dancer;
			scanf("%d", &dancer);
			if(p == 0)
			{
				ans++;
			}
			else if(p == 1)
			{
				if(dancer)
					ans++;
			}
			else if( (3*p - 2) <= dancer )
			{
				ans++;
			}
			else if( (3*p - 4) <= dancer && S) 
			{
				ans++;
				S--;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
}
