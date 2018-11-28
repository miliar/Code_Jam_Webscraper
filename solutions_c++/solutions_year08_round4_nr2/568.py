#include<cstdio>
#include<cstdlib>
int x[10],y[10];
int main()
{
	int n,m,a,abx,aby,bcx,bcy;
	bool ok;
	int t,cc,tmp;
	freopen("B-small-attempt2.in","r",stdin);
	freopen("bsuam.out","w",stdout);
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
	scanf("%d%d%d",&n,&m,&a);
		ok=0;
		if(a>=2*n*m)goto end;
				for(x[1]=0;x[1]<=n;x[1]++)
					for(y[1]=0;y[1]<=m;y[1]++)
						for(x[2]=0;x[2]<=n;x[2]++)
							for(y[2]=0;y[2]<=m;y[2]++)
							{
								abx=x[1];
								aby=y[1];
								bcx=x[2]-x[1];
								bcy=y[2]-y[1];
								if(a==abs(abx*bcy-aby*bcx))
								{
									if(0==x[1]&&0==y[1])continue;
									if(0==x[2]&&0==y[2])continue;
									if(x[1]==x[2]&&y[1]==y[2])continue;
									ok=1;
									goto end;
								}
							}
	
							
						
		end:
			printf("Case #%d: ",cc);
			if(ok)printf("%d %d %d %d %d %d\n",x[0],y[0],x[1],y[1],x[2],y[2]);
			else printf("IMPOSSIBLE\n");
		}
	return 0;
}
		
	
	
