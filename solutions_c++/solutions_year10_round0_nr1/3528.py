#include <stdio.h>

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.txt","w",stdout);
	//freopen("A-small.in","r",stdin);
	//freopen("A-small.txt","w",stdout);
	__int64 t,k,n;
	scanf("%I64d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%I64d %I64d",&n,&k);
		__int64 onnum=1;
		onnum = onnum <<n;
		k=k%onnum;
		if(k==onnum-1)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}