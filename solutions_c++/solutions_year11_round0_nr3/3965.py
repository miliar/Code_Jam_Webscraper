
#define MX 2007
#define PI 3.141592653589793238462643383279  
#define INF 100000000
#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<string.h>
#include<queue>
using namespace std;


#define e 2.718281828459 



int main()
{	int temp,sum,i,n,min,T,t;
	int O[1006];
	freopen("V.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{

		scanf("%d",&n);
		for(sum=0,min=50000000,i=1;i<=n;i++)
		{
			scanf("%d",&O[i]);
			sum+=O[i];
			if(min>O[i])
				min=O[i];
		}
		for(temp=O[1],i=2;i<=n;i++)
			temp^=O[i];

		if(temp==0)
		{
			printf("Case #%d: %d\n",t,sum-min);
		}
		else
		printf("Case #%d: NO\n",t);
	}
	return 0;
}