#include<stdio.h>

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		int n,k;
		scanf("%d%d",&n,&k);
		bool ok=1;
		for(int j=0;j<n;j++)
			if(!(k&(1<<j)))ok=0;
		if(ok)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}
