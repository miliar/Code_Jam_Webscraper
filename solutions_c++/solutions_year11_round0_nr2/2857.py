#include <stdio.h>
#include <string.h>
int main()
{
	int t,c,d,n,l=1,i,j,k,pd;
	int xq[300][300];
	char hb[300][300],str[200];
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		pd=0;
		memset(hb,0,sizeof(hb));
		memset(xq,0,sizeof(xq));
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			scanf("%s",str);
			hb[str[0]][str[1]]=str[2];
			hb[str[1]][str[0]]=str[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",str);
			xq[str[0]][str[1]]=1;
			xq[str[1]][str[0]]=1;
		}
		scanf("%d",&n);
		scanf("%s",str);
		for(i=1;i<n;i++)
		{
			for(j=i-1;j>=0;j--)
			{
				if(str[j]!=0)
					break;
			}
			if(j>=0&&hb[str[j]][str[i]])
			{
				str[i]=hb[str[j]][str[i]];
				str[j]=0;
				continue;
			}
			for(j=0;j<i;j++)
			{
				if(xq[str[i]][str[j]])
				{
					for(k=0;k<=i;k++)
						str[k]=0;
					break;
				}
			}
		}
		printf("Case #%d: [",l++);
		for(i=0;i<n;i++)
		{
			if(str[i])
			{
				if(pd==0)
				{
					pd=1;
					printf("%c",str[i]);
				}
				else 
					printf(", %c",str[i]);
			}
		}
		printf("]\n");
	}
	return 0;
}