#include<cstdlib>
#include<ctime>
#include<cstdio>
#include<cstring>
#include<sstream>
int d[10],tp,tt,mod;
char s[100];
bool mk[1024];
int ok[11][100000];
int chuli(int a)
{
	tp=0;
	while(a)
	{
		tt=a%mod;
		tp+=tt*tt;
		a/=mod;
	}
	return tp;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	srand(time(NULL));
	int cs,css,i,j,n,sum,te;
	for(te=2;te<=10000;te++)
	{
		for(i=2;i<=10;i++)
		{
			mod=i;
			sum=te;
			memset(mk,0,1024);
			while(sum!=1)
			{
				sum=chuli(sum);
				if(mk[sum])break;
				mk[sum]=true;
			}
			if(sum==1)ok[i][te]=1;
			else ok[i][te]=2;
		}
	}
	scanf("%d",&cs);getchar();
	for(css=1;css<=cs;css++)
	{
		gets(s);
		std::stringstream ss(s);n=0;
		while(ss>>d[n])
			n++;
		for(te=2;;te++)
		{
			for(i=0;i<n;i++)
			{
				mod=d[i];
				sum=chuli(te);
				if(ok[d[i]][sum]==2)break;
			}
			if(i==n)break;
		}
		printf("Case #%d: %d\n",css,te);
	}
	return 0;
}
