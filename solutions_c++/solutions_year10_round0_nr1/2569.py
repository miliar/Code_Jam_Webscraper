#include <iostream>
#include <stdlib.h>
using namespace std;
int main ()
{
	freopen("A-large.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int T;
	int i,t,n,k;
	scanf("%d",&T);
	int sum;
	for(t=1;t<=T;t++)
	{
		sum=1;
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++)sum*=2;
		k%=sum;
		if(k==sum-1)printf("Case #%d: ON\n",t);
		else printf("Case #%d: OFF\n",t);
	}
	return 0;
}