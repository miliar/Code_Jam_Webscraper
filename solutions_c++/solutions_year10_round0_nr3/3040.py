#include<iostream>

using namespace std;

int main()
{
	int t,r,k,n,test_case;
	scanf("%d",&test_case);
	for(t=0;t<test_case;t++){
		scanf("%d %d %d",&r,&k,&n);
		int people[n];
		for(int i=0;i<n;i++)
			scanf("%d",&people[i]);
		int cur=0,i,j,temp;
		long long int cost=0;
		for(int i=0;i<r;i++)
		{

//			printf("Round %d\n",t+1);
//			printf("--------\n",t+1);
			temp = k ;
			int count = 0;
			for(j=cur;j<=n;j++)
			{
				if(count>=n)
				{
					cost += (k-temp);
					cur = j;
					break;
				}
				if(j>=n)
					j=0;
				if(people[j] > temp)
				{
					cost += (k-temp);
					cur = j;
					break;
				}
//				printf("%d ",people[j]);
				temp -= people[j];
				count++;
			}
		}
		printf("Case #%d: %lld\n",t+1,cost);
	}
}

				


