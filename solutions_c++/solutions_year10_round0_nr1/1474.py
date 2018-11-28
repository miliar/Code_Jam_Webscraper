#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int two[31];

int main()
{
	int casen,i;
	int a,b;
	freopen("t1.in","r",stdin);
	freopen("t1.out","w",stdout);
	
	two[0]=1;
	for(i=1;i<=30;i++)
		two[i]=2*two[i-1];
	
	scanf("%d",&casen);
	for(i=1;i<=casen;i++)
	{
		scanf("%d %d",&a,&b);
		printf("Case #%d: ",i);
		if ((b+1)%two[a]==0)
			printf("ON\n");
		else
			printf("OFF\n");
	}

	return 0;
}
