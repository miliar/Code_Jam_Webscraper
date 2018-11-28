#include<iostream>
using namespace std;


long long int GCD(long long int a,long long int b)
{
	long long int c;
	while(b)
	{
		c=b;
		b = a%b;
		a = c;
	}
	return a;
}

long long int data[5];
int n;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.txt","w",stdout);
	int c;
	scanf("%d",&c);
	for(int i=1;i<=c;i++)
	{
		scanf("%d",&n);
		long long int min =1000000000;
		for(int j=0;j<n;j++)
		{
			scanf("%d",&data[j]);
			if(data[j]<min) min = data[j];
		}
		for(int j=1;j<n;j++)
		{
			data[j-1] = abs(data[j-1]-data[j]);
		}
		long long int gcd;
		if(n == 2)
		{
			gcd = data[0];
		}
		else
		{
			gcd = GCD(data[0],data[1]);
		}
		
		if(min %gcd==0) gcd =0;
		else gcd -= (min%gcd);

		printf("Case #%d: %lld\n",i,gcd);

	}


}