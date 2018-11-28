#include <stdio.h>
unsigned int N,K;

int main()
{
		freopen("A-large.in","r",stdin);
		//freopen("A-small-attempt0.in","r",stdin);
		freopen("Output.out","w",stdout);
	
	int testcase,result=0;
	scanf("%d",&testcase);
	
	for (int i=1;i<=testcase;i++)
	{
		scanf("%d%d",&N,&K);
		
		(K + 1) & ((2<<(N-1)) -1)?printf("Case #%d: OFF\n",i):printf("Case #%d: ON\n",i);
		
	}
	return 0;
}