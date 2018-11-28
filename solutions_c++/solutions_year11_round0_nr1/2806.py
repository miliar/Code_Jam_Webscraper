#include <stdio.h>
#include <math.h>

int main()
{
	freopen("1.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t, n, i, p;
	char r[10];
	int ot=0, bt=0, ol=1, bl=1, time =0, tmp;

	scanf("%d", &t);
	for(i=1; i<=t; i++)
	{
		scanf("%d", &n);
		time = 0, ot=0, bt=0, ol=1, bl=1;

		while(n--)
		{
			scanf("%s %d", r, &p);
			if(r[0]=='O')
			{
				if(abs(p-ol)+1<=ot)
				{
					tmp = 1;
				}
				else
				{
					tmp= abs(p-ol)-ot+1;
				}
				time += tmp;
				bt += tmp;
				ot = 0;
				ol = p;
			}
			else
			{
				if(abs(p-bl)+1<=bt)
				{
					tmp = 1;
				}
				else
				{
					tmp = abs(p-bl)-bt + 1;
					bt = 0;
				}
				time += tmp;
				ot += tmp;
				bt = 0;
				bl = p;
			}
		}
		printf("Case #%d: %d\n", i, time);
	}
	
	return 0;
}