#include <cstdio>
#include <cstring>

int main()
{
	freopen("inA.txt","r",stdin);
	freopen("outA.txt","w",stdout);
	int t,Case=1;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int tt=1<<n;
		k%=tt;
		if(k==tt-1)
			printf("Case #%d: ON\n",Case++);
		else
			printf("Case #%d: OFF\n",Case++);
	}
	return 0;
}