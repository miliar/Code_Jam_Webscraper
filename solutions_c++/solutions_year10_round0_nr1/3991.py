#include<cstdio>
#include<cstdlib>
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	int nT;
	int t=0,n,k;
	scanf("%d",&nT);
	while(nT--)
	{
		scanf("%d%d",&n,&k);	
		printf("Case #%d: ",++t);
		if(((k+1) & (1<<n)) ^ ((1<<n) & k))
			puts("ON");
		else
			puts("OFF");
	}	
}
