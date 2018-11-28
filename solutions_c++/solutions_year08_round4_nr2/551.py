#include <stdio.h>
#include <string.h>

int main() 
{
	int c;
	int n,m,a;
	int i1,j1,i2,j2,k,t;

	scanf("%d",&c);
	for(k=1;k<=c;k++)
	{
		scanf("%d%d%d",&n,&m,&a);

		for(i1=0;i1<=n;i1++)
		{
			for(j1=0;j1<=m;j1++)
			{
				for(i2=i1;i2<=n;i2++)
				{
					for(j2=0;j2<=m;j2++)
					{
						t=i1*j2-i2*j1;
						if(t==a || t==-a)
						{
							a=0;
							goto end;
						}
					}
				}
			}
		}
	
end:
		printf("Case #%d: ",k);
		if(a!=0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d %d %d %d %d %d\n",0,0,i1,j1,i2,j2);

	}

	return 0;
}
