#include <cstdio>
#include <iostream>
#include <string>
#include "BigIntegerLibrary.hh"

char numbers[1000][60];
BigInteger t[1000];

BigInteger gcd(BigInteger a, BigInteger b)
{
	if (b == 0)
		return a;
	return gcd(b, a%b);
}

int main()
{
	int c;
	scanf("%d", &c);
	int i;
	for (i = 0; i < c; i++)
	{
		int n;
		int j, k;
		BigInteger T;
		scanf("%d", &n);
		for (j = 0; j < n; j++)
			scanf("%s", numbers[j]);
		for (j = 0; j < n; j++)
		{
			t[j] = 0;
			for (k = 0; k < strlen(numbers[j]); k++)
			{
				t[j]*=10;
				t[j]+=(numbers[j][k] - '0');
			}
		}
		T = t[1]-t[0] < 0? t[0]-t[1]:t[1]-t[0];
		for (j = 1; j < n; j++)
		{
			T = gcd(T, (t[j]-t[0] < 0? t[0] - t[j]: t[j] - t[0]));
			
		}
		std::cout<<"Case #"<<i+1<<": "<<(T-(t[0]%T))%T<<"\n";
	}
}