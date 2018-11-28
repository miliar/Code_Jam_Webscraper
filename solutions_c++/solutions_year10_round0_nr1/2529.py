#include <cstdio>

int t,n,k;
int main()
{
	//freopen("in.txt","r",stdin);
	freopen("small.out","w",stdout);
	int i,ans;
	int states;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		states = 1<<n;
		ans=0;
		if (k+1>=states&&(k+1)%states==0)
			ans=1;
		printf("Case #%d: %s\n",i,ans?"ON":"OFF");
	}
	return 0;
}
