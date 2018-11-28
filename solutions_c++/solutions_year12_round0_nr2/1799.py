#include<stdio.h>
#include<algorithm>
int t[100];
main()
{
	int T,c,n,s,p,i,j;
	scanf("%d",&T);
	for(c=1;c<=T;c++)
	{
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++) scanf("%d",t+i);
		std::sort(t,t+n);
		i=std::lower_bound(t,t+n,p*3-2)-t-1;
		j=n-i-1;
		if(p>=2) p=p*3-4;
		while(t[i]>28) i--;
		while(i>=0 && s && t[i]>=p)
		{
			j++;
			s--;
			i--;
		}
		printf("Case #%d: %d\n",c,j);
	}
}
