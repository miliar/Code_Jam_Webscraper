#include<stdio.h>
#include<set>
using namespace std;
int main()
{
	int n,k,t,i;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i);
		if((k%(1<<n))==(1<<n)-1)
			printf("ON\n");
		else printf("OFF\n");

	}
	return 0;
}