#include<cstdio>
#include<cstring>

int n,k;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cases=1,t;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		int mm=1<<n;
	    k%=mm;
	    if(k+1==mm)
			printf("Case #%d: ON\n",cases++);
		else
			printf("Case #%d: OFF\n",cases++);
	}
	return 0;
}