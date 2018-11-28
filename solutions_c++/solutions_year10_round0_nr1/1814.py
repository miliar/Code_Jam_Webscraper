#include <stdio.h>
int main(){
	int n,k,t,i;
	freopen("in.txt","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&t);
	for(i = 1;i <= t;++i)
	{
		scanf("%d%d",&n,&k);
		while (n)
		{
			if(k&1)
				k/=2;
			else
				break;
			n--;
		}
		printf("Case #%d: ",i);
		if(n)
			printf("OFF\n");
		else
			printf("ON\n");
	}
	return 0;
}