#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <string>
#include <bitset>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

#define MAX 10010

using namespace std;

int n,D;
int dp[MAX][MAX];
int d[MAX],l[MAX];

int f(int pos,int prev)
{
	int i,dis;
	//cout<<"start "<<pos<<" "<<prev<<endl;
	if(pos==n) return 0;
	if(dp[pos][prev]!=-1) return dp[pos][prev];
	if(pos) dis = min( d[pos]+(d[pos] - d[prev]) , d[pos] + l[pos] );
	else dis = d[pos] + d[pos];
	//cout<<dis<<endl;
	if( dis >= D )
	{
		//cout<<"yay"<<endl;
		dp[pos][prev] = 1;
	}
	else
	{
		dp[pos][prev] = 0;
		for(i=pos+1;i<n;i++)
		{
			if( dis >= d[i] ) dp[pos][prev] = max(dp[pos][prev],f(i,pos));
			else break;
		}
	}
	return dp[pos][prev];
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-out.txt","w",stdout);
	int t,T;
	int i,j;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d %d",&d[i],&l[i]);
			for(j=0;j<n;j++)
			{
				dp[i][j]=-1;
			}
		}
		scanf("%d",&D);
		printf("Case #%d: %s\n",t,f(0,0)?"YES":"NO");
	}
	return 0;
}
