#include <stdio.h>


int main()
{
	int x0,x1,x2,y0,y1,y2,ca = 1,nCase,n,m,a,flag;
	freopen("b.in","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d",&nCase);

	while(nCase--)
	{
		scanf("%d %d %d",&n,&m,&a);
		if(n*m<a)
		{
			printf("Case #%d: IMPOSSIBLE\n",ca++);
			continue;
		}
		flag = 1;
		for(x0 = 0;x0<=n&&flag;x0++)
		{
			for(y0 = 0;y0<=m&&flag;y0++)
			{
				for(x1= 0;x1<=n&&flag;x1++)
				{
					for(y1 = 0;y1<=m&&flag;y1++)
					{
						for(x2 = 0;x2<=n&&flag;x2++)
						{
							for(y2 = 0;y2<=m&&flag;y2++)
							{
								if(((x0-x1)*(y1-y2)-(y0-y1)*(x1-x2))==a)
								{
									flag = 0;
									printf("Case #%d: %d %d %d %d %d %d\n",ca++,x0,y0,x1,y1,x2,y2);
								}
							}
						}
					}
				}
			}
		}
		if(flag)
			printf("Case #%d: IMPOSSIBLE\n",ca++);
	}
	return 0;

}