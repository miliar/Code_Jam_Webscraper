#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	
	long K;
	int N;
	
	unsigned long temp;
	
	for(int i=0;i<t;i++)
	{
		scanf("%d",&N);
		scanf("%ld",&K);
		
		temp = pow(2,N);
		if( ((K+1)%temp) == 0)
			printf("Case #%d: ON\n",(i+1));
		else
			printf("Case #%d: OFF\n",(i+1));
	}

	return 0;
}
