#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int N,K;

int main()
{
	int T;
	//freopen("A-large.in","r",stdin);
	//freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		scanf("%d%d",&N,&K);
		if((K % (1 << N)) == ((1 << N) - 1))
			printf("Case #%d: ON\n",Case);
		else
			printf("Case #%d: OFF\n",Case);
	}
	return 0;
}
