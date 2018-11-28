#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <math.h>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

#define MS(a,b) memset(a,b,sizeof(a));
#define inf 1000000000

int qs[200];
int dp[200][200];

int solve(int a,int b)
{
	if (b-a<=1)
		return 0;
	if (dp[a][b]!=-1)
		return dp[a][b];
	int res=inf,r;
	for (int i=a+1;i<b;i++)
	{
		r=qs[b]-qs[a]-2+solve(a,i)+solve(i,b);
		if (res>r)
			res=r;
	}
	return (dp[a][b]=res);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int C;
	cin>>C;
	for (int c=1;c<=C;c++)
	{
		cout<<"Case #"<<c<<": ";
		MS(qs,0);
		MS(dp,-1);
		int P,Q;
		cin>>P>>Q;
		for (int i=1;i<=Q;i++)
			cin>>qs[i];
		qs[Q+1]=P+1;
		sort(qs,qs+Q);
		cout<<solve(0,Q+1)<<endl;
	}
	return 0;
}