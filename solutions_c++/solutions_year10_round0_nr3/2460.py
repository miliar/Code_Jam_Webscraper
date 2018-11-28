#include<iostream>
using namespace std;
const int N=15*1010;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int ride,max_num,group_num;
	int group[15],array[N];
	int T,cas;
	int ans,tot_num,pos,sum;
	int i,j,remain;
	scanf("%d\n",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d%d%d",&ride,&max_num,&group_num);
		sum=0;
		for(i=0;i<group_num;i++)
		{
			scanf("%d",group+i);
			sum+=group[i];
		}
		if(sum<=max_num)
		{
			ans=sum*ride;
		}
		else
		{
			tot_num=0;
			for(i=1;i<=ride;i++)
			{
				for(j=0;j<group_num;j++)
					array[tot_num++]=group[j];
			}
			pos=0,ans=0;
			for(i=1;i<=ride;i++)
			{	
				for(remain=max_num;;pos++)
				{
					remain-=array[pos];
					ans+=array[pos];
					if(remain<0)
						break;
				}				
				ans-=array[pos];
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}