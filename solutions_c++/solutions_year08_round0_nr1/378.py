#include <stdio.h>
#include <string.h>

char name[128][128];
char sum[128];

int main() 
{
	int n,s,q;
	int x,y;
	int i,j,k;
	char t[128];

	scanf("%d",&n);
	for(x=1;x<=n;x++)
	{
		y=0;
		memset(sum,0,sizeof(sum));
		scanf("%d",&s);
		gets(t);
		for(i=0;i<s;i++)
		{
			gets(name[i]);
		}

		scanf("%d",&q);
		gets(t);
		k=0;
		for(i=0;i<q;i++)
		{
			gets(t);
			for(j=0;j<s;j++)
			{
				if(strcmp(name[j],t)==0)
				{
					if(sum[j]==0)
					{
						k++;
						if(k==s)
						{
							y++;
							k=1;
							memset(sum,0,sizeof(sum));
						}
						sum[j]=1;
					}
					break;
				}
			}
		}

		printf("Case #%d: %d\n",x,y);
	}

	return 0;
}
