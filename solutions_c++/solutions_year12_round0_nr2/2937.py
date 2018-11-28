#include "stdio.h"

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int a[101];
	int t;
	int n;
	int s;
	int p;
	scanf("%d",&t);
	int ii,i,j,k;
	for(ii=0;ii<t;ii++)
	{
		int total=0;
		int acitive=0;
		int siban=0;
		int once=0;
		int result=0;
		scanf("%d",&n);
		scanf("%d",&s);
		scanf("%d",&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&(a[i]));
			int nn=a[i]/3;
			int yu=a[i]%3;

			if(a[i]==0)
			{
				if(p==0)
				{
					once++;
					total++;
				}
				continue;
			}
			if(a[i]==1)
			{
				if(p==0||p==1)
				{
					once++;
					total++;
				}
				continue;
			}
			if(p<=nn)
			{
				total++;
				acitive++;
				continue;
			}
			if(p==(nn+1))
			{
				if(yu==0)
				{
					total++;
					siban++;
					continue;
				}
				else
				{
					total++;
					acitive++;
					continue;
				}
			}
			if(p==(nn+2))
			{
				if(yu==2)
				{
						total++;
						siban++;
						continue;
				}
				else
				{
					continue;
				}
			
			}
			if(p>=(nn+3))
			{
				continue;
			}


		}
		if(siban>=s)
		{
			result=total-(siban-s);
		}
		else
		{
	        result=total;
		}

		printf("Case #%d: %d\n",ii+1,result);
	}


	return 0;
}