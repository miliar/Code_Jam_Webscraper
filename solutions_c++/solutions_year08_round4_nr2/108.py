#include <cstdio>

int i,j,k,s,t,n,m;
int T,I;
bool f;
main()
{
	scanf("%d",&T);
	int I=0;
	while (T--)
	{
		scanf("%d%d%d",&n,&m,&s);
		printf("Case #%d: ",++I);
		f=0;
		for (i=0;i<=n;++i)
		{
			for (j=0;j<=m;++j)
			{
				for (k=0;k<=n;++k)
				{
					if (i!=0) t=(s+j*k)/i; else t=0;
					if (t*i-j*k==s&& t>=0 && t<=m)
					{
						printf("%d %d %d %d %d %d\n",0,0,i,j,k,t);
						f=1;
						break;
					}
					if (i!=0) t=(j*k-s)/i;else t=0;
					if (j*k-t*i==s && t>=0 && t<=m)
					{
						printf("%d %d %d %d %d %d\n",0,0,i,j,k,t);
						f=1;
						break;
					}
				}
				if (f) break;
			}			
			if (f) break;
		}
		if (!f) printf("IMPOSSIBLE\n"); 
	}
	return 0;
}
			
				
					
			
