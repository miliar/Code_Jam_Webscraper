#include <stdio.h>

int n,k;

inline bool ok()
{
	return ((k+1)%(1<<n))==0;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int ct,cs=1;
	scanf("%d",&ct);
	while(ct--)
	{
		printf("Case #%d: ",cs++);
        scanf("%d%d",&n,&k);
		if(ok())
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}