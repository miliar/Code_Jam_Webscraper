#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<ctime>

using namespace std;

#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define MAX(a,b)  ((a) > (b) ? (a) : (b))
#define ABS(W) ((W)<0 ? (-W) : (W))

typedef __int64 LL;
//typedef long long LL;

int R,C,memo[60][1<<10];
char grid[60][60];
vector<int> next[1<<10];

int solve(int r,int mask)
{
	int i,j,k,ret=0;
//printf("%d %d\n",r,mask);
	if(r==R) return 0;
	if(memo[r][mask]!=-1) return memo[r][mask];
	

	for(i=0;i<(1<<C);i++)
	{
		int cnt=0;
	//	i=next[mask][k];

		for(j=0;j<C;j++)
		{
			if(!(i&(1<<j)) ) continue;
			if(j>0   && (mask&(1<<(j-1)) || i&(1<<(j-1)))) break;
			if(j<C-1 && (mask&(1<<(j+1)) || i&(1<<(j+1)))) break;
			if(grid[r][j]=='x') break;
			cnt++;
		}

		if(j<C) continue;
		ret=MAX(ret,cnt+solve(r+1,i));
	}

	return  memo[r][mask]=ret;
}
int main()
{
	int i,j,k,tests,cs=0,n,m,mask;

	//freopen("C:\\","r",stdin);
	freopen("C:\\Csmall.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
	
		scanf("%d %d",&R,&C);
		for(i=0;i<R;i++)
			scanf("%s",grid[i]);
		
	
		for(i=0;i<(1<<C);i++) 
		
			next[i].clear();
			

		memset(memo,-1,sizeof(memo));

		int ans=solve(0,0);
		printf("Case #%d: %d\n",++cs,ans);
	         
	}
	return 0;
}