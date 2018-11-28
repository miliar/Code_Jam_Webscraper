#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,n,k,mul;
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&n,&k);
		mul=1<<n;
		if (k%mul==mul-1) printf("Case #%d: ON\n",cas);
		else printf("Case #%d: OFF\n",cas);
	}
}