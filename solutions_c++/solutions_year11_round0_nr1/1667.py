// poj.cpp : Defines the entry point for the console application.
//

#include <stdio.h>

int main()
{
	int t,n;
	char r;
	int p,d;
	int ol,o,bl,b;
	int i,j;
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d",&n);
		ol=bl=1;o=b=0;
		while(n--)
		{
			scanf(" %c%d",&r,&p);
			if(r=='O')
			{
				if(p-ol>=0)
					d=p-ol;
				else
					d=ol-p;
				if(o<=b)
				{
					if(b-o<=d)
						o+=d+1;
					else
						o=b+1;
				}
				else
				{
					o+=d+1;
				}
				ol=p;

			}
			else
			{
				if(p-bl>=0)
					d=p-bl;
				else
					d=bl-p;
				if(b<=o)
				{
					if(o-b<=d)
						b+=d+1;
					else
						b=o+1;
				}
				else
				{
					b+=d+1;
				}
				bl=p;
			}
		}
		printf("Case #%d: ",i+1);
		if(o>b)
			printf("%d\n",o);
		else
			printf("%d\n",b);
	}
	return 0;
}

