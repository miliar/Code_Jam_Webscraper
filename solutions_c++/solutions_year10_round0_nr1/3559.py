#include <cstdio>

int main()
{
	int nn;
	scanf("%d",&nn);
	for (int ii=1;ii<=nn;ii++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int tmp=(1<<n)-1;
		if ((k&tmp)==tmp) 
			printf("Case #%d: ON\n",ii);
		else
			printf("Case #%d: OFF\n",ii);
	}
	return 0;
}
