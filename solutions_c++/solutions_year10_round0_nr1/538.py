#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int i,t,n,k;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i);
		if(k%(1<<n)==(1<<n)-1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
