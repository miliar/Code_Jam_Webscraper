#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,k,x,d=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&n,&k);
		x=(1<<n)-1;
		k=k%(1<<n);
		printf("Case #%d: ",++d);
		if(k==x)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
