#include<cstdio>
int nsol,da,nn,a,b,t,nr,ibkp,v1,v2,inew;
int nx[21];
int main()
{
	freopen("recnum.in","r",stdin);
	freopen("recnum.out","w",stdout);
	scanf("%d",&t);
	int i,j,k;
	for(int test=1;test<=t;++test)
	{
		nsol=0;
		scanf("%d%d",&a,&b);
		for(i=a;i<=b;++i)
		{
			nn=0;
			nr=0; ibkp=i;
			while(ibkp>0)
			{
				nr++; 
				ibkp/=10;
			}
			ibkp=i;
			for(j=1;j<=nr-1;++j)
			{
				v1=1; v2=1;
				for(k=1;k<=j;++k)
					v1=v1*10;
				for(k=j+1;k<=nr;++k)
					v2=v2*10;
				inew=ibkp%v1;
				ibkp/=v1;
				ibkp=inew*v2+ibkp;
				da=1;
				/*for(k=1;k<=nn;++k)
					if(ibkp==nx[k])
						da=0;*/
				if((ibkp>i)&&(ibkp<=b)&&(da))
				{
					nsol++;
					//nn++;
					//printf("%d %d\n",i,ibkp);
				}
				
				ibkp=i;
			}
		}
		printf("Case #%d: %d\n",test,nsol);
	}
	return 0;
}