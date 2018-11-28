#include<stdio.h>
#include<iostream>
using namespace std;

int gcd(int a,int b)
{
	if (b == 0) return a;
	return gcd(b,a%b);
}

int main()
{
	int test;
	long long n;
	int b,c;
	
	scanf("%d",&test);
	for (int cas=1;cas<=test;cas++)
	{
		cin >> n >> b >> c;
		int d = gcd(b,100);
		
		int D = 100 / d;
		
		//printf("D is %d\n",D);
		printf("Case #%d: ",cas);
		if (D <= n)
		{
			if (c == 0)
			{
				if (b == 0)
					printf("Possible\n");
				else	
					printf("Broken\n");
			}else
			if (c == 100)
			{
				if (b == 100)
					printf("Possible\n");
				else
					printf("Broken\n");
			}else
				printf("Possible\n");
		}else
			printf("Broken\n");
	}
}

