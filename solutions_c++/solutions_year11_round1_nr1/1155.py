#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;

int main()
{
	long long int n, t;
	int z, d, g, zi;

	scanf("%d", &z);

	for(zi=1;zi<=z;zi++)
	{
		cin >> n >> d >> g;
		
		t = __gcd(d, 100);
		t = 100/t;

		printf("Case #%d: ", zi);

		if(t > n || (d!=100 && g==100) || (d!=0 && g==0))
			printf("Broken\n");
		else
			printf("Possible\n");
	}
}
