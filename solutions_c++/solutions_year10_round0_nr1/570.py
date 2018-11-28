#include<cstdio>
#include<cstring>

int n,k;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int ca=1,t;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		int pow=1<<n;
	    k%=pow;
	    if(k+1==pow)
			printf("Case #%d: ON\n",ca++);
		else
			printf("Case #%d: OFF\n",ca++);
	}
	return 0;
}