#include<stdio.h>

int d[100001],l[100001],f[100001];
int main()
{
	int t,bk,n,i,j,fr,to,maxd;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(bk=0;bk<t;++bk)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&maxd);
		for(i=0;i<n;++i)
			f[i]=0;
		f[0]=d[0];
		for(i=0;i<n;++i)
		{
			if(l[i]<f[i])
				f[i]=l[i];
			if(f[i]+d[i]>=maxd)
				break;
			for(j=i+1;j<n;++j)
				if(d[j]-d[i]<=f[i])
				{
					if(d[j]-d[i]>f[j])
						f[j]=d[j]-d[i];
				}
				else
					break;
		}
		if(i<n)
			printf("Case #%d: YES\n",bk+1);
		else
			printf("Case #%d: NO\n",bk+1);
	}
	return 0;
}
