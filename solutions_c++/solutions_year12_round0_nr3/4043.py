#include<cstdio>
#include<vector>
#define N 2000010

using namespace std;

vector <int> pairs[N];

int reverse(int number)
{
	int length;
	int reverse;
	char stringnum[10];
	int min=number;
	char recnum[10];
	int digit;
	length=0;
	int orgnumber=number;
	int pow=1;
	while(number>0)
	{
		length++;
		if (length!=1)
			pow*=10;
		number/=10;
	}
	
	number=orgnumber;
	for(int i=length-1;i>=0;i--)
	{
		digit=number%10;
		number/=10;
		number+=(digit*pow);
		if ((number<min) && (digit!=0))
			min=number;
	}
	return min;

}

int main()
{
	int S,A,B,T;
	int num;
	int revlow;
	for(int i=1;i<=2000000;i++)
	{
		revlow=reverse(i);
		//printf("(%d)\n",revlow);
		//if (revlow!=i)
			pairs[revlow].push_back(i);

	}
	/*
	for(int i=1;i<=1000;i++)
	{
		printf("(%d :",i);
		int z=pairs[i].size();
		for (int j=0;j<z;j++)
			printf(" %d",pairs[i][j]);
		
		printf(")\n");
	}*/
	scanf("%d",&T);
	for (int t=0;t<T;t++)
	{
		scanf("%d %d",&A,&B);
		long long int sum=0;
			
		for (int j=1;j<=B;j++)
		{
			int counter=0;
			int size=pairs[j].size();
			for (int k=0;k<size;k++)
			{
				if ((pairs[j][k]>=A) &&( pairs[j][k]<=B))
					counter++;
			}
			counter=(counter*(counter-1))/2;
			sum+=counter;
		}
		printf("Case #%d: %lld\n",t+1,sum);

	}
	return 0;
}
