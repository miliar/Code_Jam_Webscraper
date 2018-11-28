#include <stdlib.h>
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	freopen ("A-largeout.txt","w",stdout);
	int t,n,k;
	int m;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		scanf ("%d%d",&n,&k);
		m=1<<n;
		if ((k+1)%m==0) printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	}
	return 0;
}