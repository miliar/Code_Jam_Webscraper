#include "stdio.h"
#include "string.h"

char s[200][1000];
int min[1001][200];

int main()
{
	freopen("A-small-attempt0.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ca,m,n,i,j,a[1000],k,p,v;
	char s1[1000];
	scanf("%d",&ca);
	getchar();
	for(v=1;v<=ca;v++)
	{
		scanf("%d",&m);
		getchar();
		for(i=0;i<m;i++)
		{
			gets(s[i]);
		}
		scanf("%d",&n);
		getchar();
		for(i=1;i<=n;i++)
		{
			gets(s1);
			for(j=0;j<m;j++)
			{
				if(!strcmp(s[j],s1))
				{
					break;
				}
			}
			a[i]=j;
		}
		for(i=0;i<m;i++)
		{
			min[0][i]=0;
		}
		for(i=1;i<=n;i++)
		{
			for(j=0;j<m;j++)
			{
				min[i][j]=min[i-1][j];
				if(a[i]==j)
				{
					min[i][j]=999999;
				}
				else if(a[i-1]==j)
				{
					for(k=0;k<m;k++)
					{
						if(min[i-1][k]+1<min[i][j])
						{
							min[i][j]=min[i-1][k]+1;
						}
					}
				}
			}
		}
		p=999999;
		for(i=0;i<m;i++)
		{
			if(min[n][i]<p)
			{
				p=min[n][i];
			}
		}
		printf("Case #%d: %d\n",v,p);
	}
	return 0;
}