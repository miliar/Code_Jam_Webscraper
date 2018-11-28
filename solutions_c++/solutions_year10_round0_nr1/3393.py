#include <stdio.h>

int main()
{
	freopen("a.out.txt","w",stdout);
	freopen("a.in.txt","r",stdin);
	int kase, tCase = 0;
	scanf ("%d",&kase);

	while (kase--)
	{
		int li, tog, flag = 1, res;
		scanf ("%d%d", &li, &tog);
		res = (1<<li)-1;
		if ((res & tog) == res)
			printf ("Case #%d: ON\n",++tCase);
		else
			printf ("Case #%d: OFF\n",++tCase);
		/*
		for (int i=0; i<li; i++)
			if ( (1<<i)&tog == 0)
			{
				 printf ("Case #%d: OFF\n",++tCase);
				 flag = 0;
				 break;
			}
		if (flag) printf ("Case #%d: ON\n",++tCase);*/
	}
	
	return 0;
}