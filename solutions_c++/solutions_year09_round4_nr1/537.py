#include "stdio.h"
int main()
{
	char ch;
	int t,i,k,j,n,kase,x[45],b,l;
	scanf("%d",&t);
	for(kase=1;kase<=t;kase++)
	{
		scanf("%d",&n);
		getchar();
		for(i=1;i<=n;i++)
		{
			j=0;
			for(k=1;k<=n;k++)
			{
				ch=getchar();
				if(ch=='1')
					j=k;
			}
			getchar();
			x[i]=j;
		}
		b=0;
		for(i=1;i<n;i++)
		{
			while(1)
			{
				if(x[i]>i)
				{
					j=x[i];
					for(k=i+1;k<=n;k++)
					{
						if(x[k]<=i)
						{
							b++;
							x[i]=x[k];
							x[k]=j;
							break;
						}
						l=x[k];
						x[k]=j;
						j=l;
						b++;
					}
				}
				else
					break;
			}
		}
		printf("Case #%d: %d\n",kase,b);
	}
	return 0;
}