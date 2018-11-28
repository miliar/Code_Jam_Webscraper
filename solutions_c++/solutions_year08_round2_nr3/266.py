#include<iostream>
using namespace std;
int list[5010];
int main()
{
	int T ,i , j , k , K ;
	int cases ;
	int num , id ;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	while(1 ==scanf("%d",&T))
	{
		for(cases=1;cases<=T;cases++)
		{
			scanf("%d",&K);
			for(i=1;i<=K;i++)
				list[i]=0;
			int s = 1 ;
			for(i=1;i<=K;i++)
			{
				int sum=0;
				for(j=s; ;j++)
				{
					if(j>K) 
						j-=K;
					if(j==0)		continue;
					if(list[j])	continue;
					sum++;
					if(sum==i)
					{
						list[j]=i;
						s = j ;
						break;
					}
				}
			}
			scanf("%d",&num);
			printf("Case #%d:",cases);
			for(i=1;i<=num;i++)
			{
				scanf("%d",&id);
				printf(" %d",list[id]);
			}
			printf("\n");
		}
		
	}
	return 0 ; 
}