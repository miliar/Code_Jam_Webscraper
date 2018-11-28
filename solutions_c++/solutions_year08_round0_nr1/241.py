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

int cases,caseno,n,m;
char a[105][105],q[1005][105];
int st[105][1005],dp[105][1005];

void input()
{
	int i;

	scanf("%d",&n);
	gets(a[0]);
	for(i=0;i<n;i++) gets(a[i]);
	scanf("%d",&m);
	gets(q[0]);
	for(i=0;i<m;i++) gets(q[i]);
}

inline int min(int a,int b)
{
	return (a<b) ? a : b;
}

int call(int ith,int qth)
{
	if(qth==m) return 0;
	if(st[ith][qth]==caseno) return dp[ith][qth];
	st[ith][qth]=caseno;

	if(strcmp(a[ith],q[qth])) dp[ith][qth]=call(ith,qth+1);
	else
	{
		dp[ith][qth]=1000000000;
		for(int i=0;i<n;i++) if(i!=ith) dp[ith][qth]=min(dp[ith][qth],1+call(i,qth+1));
	}
	return dp[ith][qth];
}

void process()
{
	int mn=1000000000,i;

	caseno++;
	for(i=0;i<n;i++) mn=min(mn,call(i,0));
	printf("Case #%d: %d\n",caseno,mn);
}

int main()
{
	//freopen("Inputs\\A-large.in","r",stdin);
	//freopen("Inputs\\A1.ans","w",stdout);

	scanf("%d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}