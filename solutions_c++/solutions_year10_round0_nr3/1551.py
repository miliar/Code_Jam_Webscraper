#include<stdio.h>
#include<string.h>
int i,j,k,n,m,g[1010],t,v,b[1010],p,c[1010],d[1010],r;
long long total,a[1010];
main()
{
	freopen("C-large.in","r",stdin);freopen("w.txt","w",stdout);
	scanf("%d",&t);
	for(v=1;v<=t;v++)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(c,0,sizeof(c));
		memset(d,0,sizeof(d));
		
		printf("Case #%d: ",v);
		scanf("%d%d%d",&r,&k,&n);
		for(i=1;i<=n;i++){
			scanf("%d",&g[i]);
		}
		for(i=1;i<=n;i++){
			p=0;
			j=i;
			while(p+g[j]<=k)
			{
				p=p+g[j];
				j++;
				if(j>n)j=1;
				if(j==i)break;
			}
			c[i]=p;
			b[i]=j;
		}
		j=1;
		total=0;
		for(i=1;i<=r;i++){
			total=total+c[j];
			j=b[j];
			if(d[j]>0&&(r-i)%(i-d[j])==0)
				break;
			a[j]=total;
			d[j]=i;
		}
		total=total+(total-a[j])*((long long)(r-i)/(i-d[j]));
		printf("%lld\n",total);				
	}
} 
