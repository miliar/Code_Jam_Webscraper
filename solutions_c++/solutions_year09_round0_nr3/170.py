#include<stdio.h>
#include<string.h>
#define mod 10000
#define len 19
char s[len+1]="welcome to code jam";
char s1[1000];
int ans[len][1000];

void solve()
{
	gets(s1);
	int l=strlen(s1);
	for(int i=0;i<l;++i)
		ans[0][i]=(s1[i]==s[0]);
	for(int i=1;i<len;++i)
	{
		int num=0;
		for(int j=0;j<l;++j)
		{
			if(s1[j]==s[i])
				ans[i][j]=num;
			else ans[i][j]=0;
			num+=ans[i-1][j];
			if(num>=mod) num-=mod;
		}
	}
	int sum=0;
	for(int i=0;i<l;++i)
	{
		sum+=ans[len-1][i];
		if(sum>=mod) sum-=mod;
	}
	int p[4];
	p[0]=sum/1000;
	sum%=1000;
	p[1]=sum/100;
	sum%=100;
	p[2]=sum/10;
	sum%=10;
	p[3]=sum;
	printf("%d%d%d%d\n",p[0],p[1],p[2],p[3]);
}

int main()
{
	int t;
	scanf("%d",&t);
	gets(s1);
	for(int i=0;i<t;++i)
	{
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}

