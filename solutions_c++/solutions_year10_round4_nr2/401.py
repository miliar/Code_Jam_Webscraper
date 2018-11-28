#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large(2)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


int mas[2000][2000];
int  col[2010];
int p;
long long dp[1050][1050][12];
long long oo=1LL<<50;

long long go(int x, int y, int t)
{
	if (x==0)
	{
		if (col[y]>=t) return 0;
		return oo;
	}
	if (dp[x][y][t]!=-1) return dp[x][y][t];
	long long res=oo;
	res = mas[x][y] + go(x-1,2*y,t) + go(x-1,2*y+1,t);
	res = min(res, go(x-1,2*y,t+1) + go(x-1,2*y+1,t+1));

	return dp[x][y][t] = res;
}
int main()
{
	init();	
	

	int tst;
	scanf("%d",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
		scanf("%d",&p);
		memset(dp,-1,sizeof(dp));

		for (int i=0;i<1<<p;i++)
			scanf("%d",&col[i]);

		for (int i=1;i<=p;i++)
		{
			for (int j=0;j<(1<<(p-i));j++)
				scanf("%d",&mas[i][j]);
		}
		
		long long res = go(p,0,0);
		
		printf("Case #%d: %lld\n",cas,res);
	
	}
	



	
  return 0;
}
