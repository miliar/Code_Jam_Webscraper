#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("gca3.txt","w",stdout);
	int i=0,t=0,n=0,k=0,ar[50];
	ar[0]=1;
	for(i=1;i<31;i++)
	ar[i]=ar[i-1]*2;
	scanf("%d",&t);
	i=1;
	while(i<=t)
	{
		scanf("%d %d",&n,&k);		
		printf("Case #%d: ",i); 
		if((k+1)%ar[n]==0)
		printf("ON\n");
		else
		printf("OFF\n");
		++i;
	}
	return 0;
}
