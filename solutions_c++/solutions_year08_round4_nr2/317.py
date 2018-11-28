#include<stdio.h>
#include<math.h>
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int c,o,n,m,a,x1,x2,y1,y2,now,x,y;
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		scanf("%d%d%d",&n,&m,&a);
		for(x1=-n;x1<=n;x1++)
			for(y2=-m;y2<=m;y2++)
				for(x2=-n;x2<=n;x2++)
				{
					now=x1*y2-a;
					if(!x2||now%x2)
						continue;
					y1=now/x2;
					if(abs(y1)>m||abs(x1-x2)>n||abs(y1-y2)>m)
						continue;
					x=0;
					if(x1<x)
						x=x1;
					if(x2<x)
						x=x2;
					y=0;
					if(y1<y)
						y=y1;
					if(y2<y)
						y=y2;
					printf("Case #%d: %d %d %d %d %d %d\n",o,-x,-y,x1-x,y1-y,x2-x,y2-y);
					goto will;
				}
		printf("Case #%d: IMPOSSIBLE\n",o);
		will:;
	}
	return 0;
}