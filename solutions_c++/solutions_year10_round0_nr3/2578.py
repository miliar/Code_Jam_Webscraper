#include <iostream>
using namespace std;


int main()
{
	freopen("d:\\A-large.in", "r", stdin);
	freopen("d:\\A-large.out", "w", stdout);

	int t,n,k,i,j,r;
	int g[2000],sum,cnt;

	scanf("%d",&t);

	for(i=1;i<=t;i++)
	{
		scanf("%d%d%d",&r,&k,&n);

			sum=0;
		cnt=0;
	for(j=0;j<n;j++)
		scanf("%d",&g[j]);

	int pos=1%n;
	j=1%n;
	sum=g[0];
	while (r)
	{


		if (pos==(j+1)%n)
		{
			r--;
			cnt+=sum;
			sum=g[j];
			pos=(j+1)%n;
		}
		else if(g[j]+sum>k)
		{
			r--;
			cnt+=sum;
			sum=g[j];
			pos=(j+1)%n;
		}	
		else sum+=g[j];

		j=(j+1)%n;

	}

	
		
		printf("Case #%d: %d\n",i,cnt);
	}




	return 0;
}