#include <stdio.h>
#include <stdlib.h>

class point
{
public:
	int x,y;
};

int main()
{
	int t;
	point p1,p2;
	int e,f;
	int i;
	int cas,asd;
	int a,n,m;
	int solve;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d %d %d",&n,&m,&a);
		solve=0;
		printf("Case #%d: ",asd+1);
		
		for(p1.x=0;p1.x<=n;p1.x++)
		{
			for(p1.y=0;p1.y<=m;p1.y++)
			{
				for(p2.x=0;p2.x<=n;p2.x++)
				{
					for(p2.y=0;p2.y<=m;p2.y++)
					{
						t = abs(p1.x * p2.y - p2.x * p1.y);
						if(t==a)
						{
							solve = 1;
							printf("%d %d %d %d %d %d\n",0,0,p1.x,p1.y,p2.x,p2.y);
							break;
						}
					}
					if(solve)
						break;
				}
				if(solve)
					break;
			}
			if(solve)
				break;
		}

		if(solve==0)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}