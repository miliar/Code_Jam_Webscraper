#include<stdio.h>
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int n,i,j;
	int num,s_num,cut,sum[110],result;

	scanf("%d",&n);

	for(i=0;i<n;i++)
	{
		result=0;
		scanf("%d %d %d",&num,&s_num,&cut);
		for(j=0;j<num;j++)
		{
			scanf("%d",&sum[j]);
			if(sum[j]>=3*cut-2)
			{
				result++;
			}
			else
			{
				if(sum[j]>=3*cut-4 && s_num>0)
				{
					if(sum[j]-cut>=0)
					{
						s_num--;
						result++;
					}
				}
			}
		}
		printf("Case #%d: %d\n",i+1,result);
	}
	
	return 0;
}