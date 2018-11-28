#include<stdio.h>
#include<string.h>

char a[510],b[]={"welcome to code jam"};
int vi[510][25],dp[510][25];

int func(int i,int j)
{
	if(j==19)
		return 1;
	if(a[i]==0)
	{
		return 0;
	}
	if(vi[i][j])
		return dp[i][j];
	int r=0;
	if(a[i]==b[j])
		r+=(func(i+1,j+1))%10000;
	r+=(func(i+1,j))%10000;
	vi[i][j]=1;
	dp[i][j]=r%10000;
	return dp[i][j];
}

int main()
{
	//freopen("C-large.in","r",stdin);
	//freopen("Cl.out","w",stdout);
	int cs,t=1,x;
	scanf("%d",&cs);
	getchar();
	while(cs--)
	{
		gets(a);
		memset(vi,0,sizeof(vi));
		x=func(0,0);
		printf("Case #%d: %04d\n",t++,x%10000);
	}
	return 0;
}