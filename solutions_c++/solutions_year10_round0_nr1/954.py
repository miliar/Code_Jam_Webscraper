#include <cstdio>

int i,j,k,s,t,n,m;
int T,I;

main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		scanf("%d%d",&n,&m);
		printf("Case #%d: ",I);
		if ((m+1)%(1<<n)==0)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
