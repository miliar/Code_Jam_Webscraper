#include <iostream>
using namespace std;

int n,k;
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int cas,casid=0;
	scanf("%d",&cas);
	while(cas--)
	{
		scanf("%d%d",&n,&k);
		int mod=1<<n;
		k=k%mod;
		if(k==mod-1)printf("Case #%d: ON\n",++casid);
		else printf("Case #%d: OFF\n",++casid);
	}
}