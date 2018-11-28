#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int t,cas;
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(cas=1;cas<=t;++cas)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",cas);
		int kl=1;
		for(int i=0;i<n;++i)
			kl*=2;
		k=k%kl;
		if(k==kl-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
}