#include <iostream>
#include <cstring>
using namespace std;
int n,k,T,t,a,b;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&k);
		a=(1<<n);
		b=a-1;
		printf("Case #%d: ",t);
		if (k%a==b) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}