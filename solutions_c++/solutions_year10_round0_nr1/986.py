#include<cstdio>
#include<memory>
#include <math.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int t,n,k;
	scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		scanf("%d%d",&n,&k);
		int x= 1<<n;
		int out = k%x;
		printf("Case #%d: ",i);
		if(out == x-1)
		{
			printf("ON\n");
		}
		else printf("OFF\n");
	}
	return 0;
}