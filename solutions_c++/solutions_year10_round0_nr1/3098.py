#include <stdio.h>

int n,k;

int main()
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	int cas=1;
	while(T--)
	{
		scanf("%d%d",&n,&k);
		int temp;
		temp=1<<n;
	    k%=temp;
		int ans;
		if(k==(temp-1))
			ans=1;
		else
			ans=0;
	    if(ans)
	    {
	        printf("Case #%d: ON\n",cas);
	    }
	    else
	    {
	        printf("Case #%d: OFF\n",cas);
	    }
		cas++;
	}
	return 0;
}