#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define i64 __int64

#define MAX 100001
#define inf 200000000

int cases,caseno;
int m,v,gate[MAX],ch[MAX],dp[MAX][3],st[MAX][3];

int min(int a,int b)
{
	return (a<b) ? a : b;
}

void input()
{
	int i,k=1;

	scanf("%d %d",&m,&v);
	for(i=0;i<(m-1)/2;i++)
	{
		scanf("%d %d",&gate[k],&ch[k]);
		k++;
	}
	for(i=0;i<(m+1)/2;i++)
	{
		ch[k]=-1;
		scanf("%d",&gate[k]);
		k++;
	}
}

int call(int i,int val)
{
	if(ch[i]==-1)
	{
		if(gate[i]==val) return 0;
		return inf;
	}
	if(st[i][val]==caseno) return dp[i][val];
	st[i][val]=caseno;

	dp[i][val]=inf;

	int x1,x2,x3,x4;

	x1=call(2*i,0);
	x2=call(2*i+1,0);
	x3=call(2*i,1);
	x4=call(2*i+1,1);

	if(gate[i]==1)
	{
		if(val==1)
		{
			dp[i][val]=min(dp[i][val],x3+x4);
			if(ch[i]==1)
			{
				dp[i][val]=min(dp[i][val],1+x1+x4);
				dp[i][val]=min(dp[i][val],1+x2+x3);
				dp[i][val]=min(dp[i][val],1+x3+x4);
			}
		}
		else
		{
			dp[i][val]=min(dp[i][val],x1+x4);
			dp[i][val]=min(dp[i][val],x2+x3);
			dp[i][val]=min(dp[i][val],x1+x2);
			if(ch[i]==1)
			{
				dp[i][val]=min(dp[i][val],1+x1+x2);
			}
		}
	}
	else
	{
		if(val==0)
		{
			dp[i][val]=min(dp[i][val],x1+x2);
			if(ch[i]==1)
			{
				dp[i][val]=min(dp[i][val],1+x1+x4);
				dp[i][val]=min(dp[i][val],1+x2+x3);
				dp[i][val]=min(dp[i][val],1+x1+x2);	
			}
		}
		else
		{
			dp[i][val]=min(dp[i][val],x1+x4);
			dp[i][val]=min(dp[i][val],x2+x3);
			dp[i][val]=min(dp[i][val],x3+x4);
			if(ch[i]==1)
			{
				dp[i][val]=min(dp[i][val],1+x3+x4);
			}
		}
	}

	return dp[i][val];
}

void process()
{
	int res;

	printf("Case #%d: ",++caseno);
	res=call(1,v);
	if(res==inf) puts("IMPOSSIBLE");
	else printf("%d\n",res);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a1.ans","w",stdout);
		
	scanf("%d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}
