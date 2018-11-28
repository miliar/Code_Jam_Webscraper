#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main()
{
	long long int t;
	cin >> t;
	for(int i=0;i<t;i++)
	{
		//initialize
		long long int n,k;
		cin >> n >> k;
		long long int x=pow(double(2),double(n));

		printf("Case #%d: ",i+1);
		if((k%x)+1==x)
		{
			printf("ON\n");
		}
		else
		{
			printf("OFF\n");
		}
	}
	return 0;
}
