#include<stdio.h>
#include<memory.h>
#include<string.h>
int main()
{
	int j,k,l,result,t,n,s,q,i;
	char SearchEngine[110][110];
	char buffer[110];	
	int sum[1024][110];		
	scanf("%d",&n);
	for(l=1;l<=n;l++)
	{
		memset(sum,0,sizeof(sum));
		memset(buffer,0,sizeof(buffer));
		memset(SearchEngine,0,sizeof(SearchEngine));
		scanf("%d\n",&s);
		for(i=0;i<s;i++)
		{
			gets(SearchEngine[i]);			
		}
		scanf("%d\n",&q);
		for(i=1;i<=q;i++)
		{
			gets(buffer);								
			for(j=0;j<s;j++)
			{
				if(strcmp(buffer,SearchEngine[j])==0){t=j;break;}
			}			
			for(j=0;j<s;j++)
			{
				result=9999999;
				for(k=0;k<s;k++)
				{
					if(k!=j && sum[i-1][k]<result) result=sum[i-1][k];
				}				
				result++;
				if(j==t || sum[i-1][j]>=result)	sum[i][j]=result;
				else sum[i][j]=sum[i-1][j];
			}
		}
		result=9999999;
		for(i=0;i<s;i++)if(sum[q][i]<result)result=sum[q][i];
		printf("Case #%d: %d\n",l,result);
	}
	return 0;
}