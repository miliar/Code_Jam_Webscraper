#include<iostream>
using namespace std;
int main()
{
	int cases,t;
	int m,n,a;
	int i,j,x,y;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cases);
	for(t=1;t<=cases;++t)
	{
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d: ",t);
		if(a>m*n)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		for(i=0;i<=n;++i)
		{
			for(j=0;j<=m;++j)
			{
				for(x=0;x<=n;++x)
				{
					for(y=0;y<=m;++y)
					{
						if(abs(i*y-x*j)==a)
						{
							printf("%d %d %d %d %d %d\n",0,0,i,j,x,y);
							goto ex;
						}
					}
				}
			}
		}
ex:
		if(i>n)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}