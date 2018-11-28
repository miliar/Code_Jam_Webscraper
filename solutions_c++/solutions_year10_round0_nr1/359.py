#include <iostream>
using namespace std;

int main()
{
	int t,n,k;
	scanf("%d",&t);
	for (int i=0;i<t;i++)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i+1);
		k%=(1<<n);
		if (k==(1<<n)-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}