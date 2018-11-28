#include<stdio.h>
#include<string.h>

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int ca,t,n,k,i,j;
	scanf("%d",&t);
	for(ca=1;ca<=t;ca++){
		scanf("%d%d",&n,&k);
		for(i=j=1;i<=n;i++)j<<=1;
		if((k+1)%j==0)
			printf("Case #%d: ON\n",ca);
		else printf("Case #%d: OFF\n",ca);
	}
	return 0;
}