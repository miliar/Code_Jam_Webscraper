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

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define i64 __int64
#define inf 1000000000

const double eps = 1e-11;

#define MOD 10007

int cases,caseno;

int m,n,k,dp[101][101],st[101][101];
bool gr[101][101];

void input()
{
	int x,y;

	CLR(gr);
	scanf("%d %d %d",&m,&n,&k);
	for(int i=0;i<k;i++)
	{
		scanf("%d %d",&x,&y);
		gr[x][y]=true;
	}
}

int call(int x,int y)
{
	if(x<=0 || y<=0) return 0;
	if(x==1 && y==1) return 1;
	if(gr[x][y]) return 0;
	if(st[x][y]==caseno) return dp[x][y];

	st[x][y]=caseno;

	dp[x][y]=(call(x-1,y-2)+call(x-2,y-1))%MOD;

	return dp[x][y];
}

void process()
{
	printf("Case #%d: ",++caseno);
	printf("%d\n",call(m,n));
}

int main()
{
	freopen("Inputs\\d.in","r",stdin);
	freopen("Inputs\\d1.txt","w",stdout);

	scanf("%d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}
