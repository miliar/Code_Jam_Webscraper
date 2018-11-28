#include <iostream>
using namespace std;
int main()
{
	int t,i;
	int n,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	int x;
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		x=(2<<(n-1));
		if ((k+1)%x==0)
		{
			printf("Case #%d: ON\n",i);
		}
		else printf("Case #%d: OFF\n",i);		
	}
	return 0;
}