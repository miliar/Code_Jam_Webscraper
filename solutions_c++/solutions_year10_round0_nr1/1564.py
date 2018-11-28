#include<stdio.h>
main()
{
	int i,j,k,m,n,t,p;
	freopen("A-large.in","r",stdin);freopen("w.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d%d",&n,&k);
		p=1<<n;
		while(k>=p)k-=p;
		printf("Case #%d: ",i);
		if(k==p-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	
} 
