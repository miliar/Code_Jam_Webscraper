#include <stdio.h>

int power(int i)
{
	if(i==0)return 1;
	return 2*power(i-1);
}

void main()
{
	int T;
	scanf("%i",&T);
	for(int i=1;i<=T;i++)
	{
		int N,K,p2;
		scanf("%i%i",&N,&K);
		p2=power(N);
		printf("Case #%i: ", i);
		if(K-p2+1<0)printf("OFF\n");
		else if(((K-p2)+1)%p2)printf("OFF\n");
		else printf("ON\n");
	}
}