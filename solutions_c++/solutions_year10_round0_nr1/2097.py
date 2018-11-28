#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
	int t;
	int i,n,k;
	scanf("%d",&t);
	for(i=0;i<t;++i)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i+1);
		if((k+1)%(1<<n)==0)
			printf("ON\n");
		else
			printf("OFF\n");
	}
}
