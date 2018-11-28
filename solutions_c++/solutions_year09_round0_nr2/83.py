#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <map>
#include <set>
#include <cassert>
#include <list>
#include <deque>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <queue>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b)) 
#define SETF(x) memset(x,0xff,sizeof(x))
#define SET0(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB(x) push_back(x)
#define VI vector <int> 
#define VVI vector < vector <int> > 
#define VS vector <string>
 
using namespace std;

int grid[101][101];
char ans[101][101];
int H,W;
int visited[101][101];
char curr;
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
char solve(int m, int n)
{
	if(ans[m][n]!='#')
		return ans[m][n];
	visited[m][n]=1;
	int k;
	int minl=grid[m][n],minx,miny;
	for(k=0;k<4;k++)
	{
		int x=m+dx[k];
		int y=n+dy[k];
		if(x>=0 && x<H && y>=0 && y<W && grid[x][y]<minl)
		{
			if((visited[x][y]==0 && ans[x][y]=='#') || (visited[x][y]==1 && ans[x][y]!='#'))
			{
				minl=grid[x][y];
				minx=x;
				miny=y;
			}
		}
	}
	if(minl!=grid[m][n])
		return ans[m][n]=solve(minx,miny);
	return ans[m][n]=curr++;
}
void display()
{
	int i,j;
	for(i=0;i<H;i++)
	{
		for(j=0;j<W;j++)
			cout<<ans[i][j]<<" ";
		cout<<endl;
	}
}
int main()
{
	int T;
	int cas=1;
	cin>>T;
	while(T--)
	{
		SET0(visited);
		curr='a';
		cin>>H>>W;
		int i,j;
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				cin>>grid[i][j];
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				ans[i][j]='#';
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				ans[i][j]=solve(i,j);
		cout<<"Case #"<<cas<<": "<<endl;
		display();
		cas++;
	}
	return 0;
}
