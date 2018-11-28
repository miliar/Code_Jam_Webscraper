#include <stdio.h>

int Fabs(int a)
{
	return a>0?a:-a;
}
int f(int x1,int y1,int x2,int y2,int x3,int y3)
{
	return Fabs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1));
}
int main()
{
	int aCase,i,j,x1,x2,x3,y1,y2,y3,n,m,a;
	scanf("%d",&aCase);
	for(int tt=1;tt<=aCase;tt++)
	{
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d: ",tt);
				for(x2=0;x2<=n;x2++)
					for(y2=0;y2<=m;y2++)
						for(x3=0;x3<=n;x3++)
							for(y3=0;y3<=m;y3++)
								if(f(0,0,x2,y2,x3,y3)==a)
								{
									printf("0 0 %d %d %d %d\n",x2,y2,x3,y3);
									goto label;	
								}
		printf("IMPOSSIBLE\n");
label:;
	}
}
