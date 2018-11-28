#include<iostream>
using namespace std;

int bin[31];
int n,k,t;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Al.out","w",stdout);
	bin[0]=1;
	for(int i=1;i<=30;++i)
	{
		bin[i]=bin[i-1]<<1;
	}
	scanf("%d",&t);
	for(int ca=1;ca<=t;++ca)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",ca);
		if((k+1)%bin[n]==0)
		{
			puts("ON");
		}
		else
		{
			puts("OFF");
		}
	}
	return 0;
}
