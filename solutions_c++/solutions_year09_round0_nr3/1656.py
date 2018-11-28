#include<cstdio>
#include<cstring>

const int MOD=10000;
#define M 505
char a[M];
char *p="welcome to code jam";
int plen=strlen(p);
int alen;
int memo[20][M];

int fun(int x,int y)
{
	if(memo[x][y]!=-1)
		return memo[x][y];
	if(x==plen)
		return 1;
	if(y==alen)
		return 0;
	int ans=0;
	int i;
	for(i=y;i<alen;++i)
		if(a[i]==p[x])
			ans=(ans+fun(x+1,i+1))%MOD;
	return memo[x][y]=ans;
}
int main()
{
	int n;
	scanf("%d",&n);
	gets(a);
	int t;
	for(t=1;t<=n;++t)
	{
		gets(a);
		alen=strlen(a);
		memset(memo,-1,sizeof(memo));
		printf("Case #%d: %04d\n",t,fun(0,0));
	}
	return 0;
}
