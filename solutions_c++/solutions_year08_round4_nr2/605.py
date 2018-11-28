#include "stdio.h"

int abs(int a)
{
	if(a>0)
	{
		return a;
	}
	return a*-1;
}

int main()
{
	freopen("small.txt","r",stdin);
	freopen("small_out.txt","w",stdout);
	int v,ca,m,n,a,x1,x2,x3,y1,y2,y3,s;
	scanf("%d",&ca);
	for(v=1;v<=ca;v++)
	{
		scanf("%d%d%d",&m,&n,&a);
		s=-1;
		for(x1=0;x1<=m;x1++)
		{
			for(y1=0;y1<=n;y1++)
			{
				for(x2=0;x2<=m;x2++)
				{
					for(y2=0;y2<=n;y2++)
					{
						s=abs(x1*y2-x2*y1);
						if(s==a)
						{
							break;
						}
					}
					if(s==a)	break;
				}
				if(s==a)	break;
			}
			if(s==a)	break;
		}
		printf("Case #%d: ",v);
		if(s==a)
		{
			printf("0 0 %d %d %d %d\n",x1,y1,x2,y2);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}