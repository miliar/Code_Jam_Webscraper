#include <iostream>
using namespace std;
int cases,ncase,i,k,n,now;
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	scanf("%d",&cases);
	for (ncase=0; ncase<cases; ncase++)
	{
		scanf("%d%d",&n,&k);
		now = 1;
		for (i=0; i<n; i++)
			now = now*2;
		if ((k+1)%now==0)
			printf("Case #%d: ON\n",ncase+1);
		else
			printf("Case #%d: OFF\n",ncase+1);
	}
	return 0;
}