#include <string.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
bool b[109];
int main()
{
	int Q,n,K,M;
	scanf("%d",&Q);
	for(int t=1;t<=Q;t++)
	{
		scanf("%d%d",&n,&K);
		M=1<<n;
		K%=M;
		int cnt=0;
		printf("Case #%d: ",t);
		if(K==M-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
