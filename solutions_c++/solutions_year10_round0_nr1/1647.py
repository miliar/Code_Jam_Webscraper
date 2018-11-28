#include <cstdio>
#include <cstring>

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,ca=1;
	scanf("%d",&t);
	while(t--)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		k%=(1<<n);
		if(k==((1<<n)-1)) printf("Case #%d: ON\n",ca++);
		else printf("Case #%d: OFF\n",ca++);
	}
	return 0;
}