#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) (a*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
int cases,z;
int h,w;
int grid[109][109];
char ans[109][109];
bool vis[109][109];
char cnt;
int dx[]={0,-1,1,0};
int dy[]={-1,0,0,1};
inline bool chk(int y,int x)
{
	return (y>=0 && y<h && x<w && x>=0);
}
char go(int y,int x)
{
	if(vis[y][x])return ans[y][x];
	vis[y][x]=1;
	int ma=1<<20,ny,nx,bi,i;
	for(i=3;i>=0;i--)
	{
		ny=dy[i]+y;
		nx=dx[i]+x;
		if(chk(ny,nx))
		{
			if(ma>=grid[ny][nx])
				ma=grid[ny][nx],bi=i;
		}
	}
	if(ma==1<<20 || ma>=grid[y][x])
	{
		ans[y][x]=cnt++;
	}
	else
	{
		ans[y][x]= go(dy[bi]+y,dx[bi]+x);
	}
	return ans[y][x];
}
int main()
{
	#ifdef WIN32
		freopen("B-large.in","r",stdin);
		freopen("B-large.out","w",stdout);
	#endif
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(z=1;z<=cases;z++)
	{
		CLS(vis,0);
		scanf("%d%d",&h,&w);
		cnt='a';
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
			{
				scanf("%d",&grid[i][j]);
			}
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
			{
				ans[i][j]=go(i,j);
			}
		printf("Case #%d:\n",z);
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
				printf("%c ",ans[i][j]);
			printf("\n");
		}
	}
	return 0;
}