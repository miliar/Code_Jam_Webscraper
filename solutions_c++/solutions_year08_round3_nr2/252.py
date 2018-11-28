#include <iostream>
#include <string>
using namespace std;

char tstr[100];
int count=0;
int sign[100];
int len;

int ugly(__int64 x)
{
	if(x<0) x=-x;
	if(x%2==0) return 1;
	if(x%3==0) return 1;
	if(x%5==0) return 1;
	if(x%7==0) return 1;
	return 0;
}
void dfs(int x)
{
	if(x==len-1)
	{
		__int64 result=0;
		__int64 tval=0;
		int lastop=0;
		for(int i=0;i<len;i++)
		{
			tval*=10;
			tval+=tstr[i]-'0';
			if(sign[i])
			{
				if(lastop==0) result+=tval;
				else result -= tval;
				tval=0;
				if(sign[i]==1) lastop=0;
				else if(sign[i]==-1) lastop=1;
			}
		}
		if(lastop==0) result+=tval;
		else result -=tval;

		if(ugly(result)) count++;
		return;
	}
	for(int i=-1;i<=1;i++)
	{
		sign[x]=i;
		dfs(x+1);
	}
}
int solve()
{
	len=strlen(tstr);
	count=0;
	dfs(0);
	return count;
}

int main()
{
	//freopen("B_small.in","r",stdin);
	//freopen("B_small.out","w",stdout);

	int T,Ti;
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++)
	{
		printf("Case #%d: ",Ti);
		scanf("%s",tstr);
		printf("%d",solve());

		puts("");
	}
}