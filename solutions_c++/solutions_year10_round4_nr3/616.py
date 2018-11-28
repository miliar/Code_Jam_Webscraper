#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;
#define maxn 105
bool maps[maxn][maxn];
bool mapb[maxn][maxn];
int maxx,maxy;

void init()
{
	for(int i=0;i<maxn;i++)
		for(int j=0;j<maxn;j++)
			mapb[i][j]=maps[i][j]=0;
	maxx=maxy=0;
	int r;
	cin>>r;
	int x1,x2,y1,y2;
	while(r--)
	{
		cin>>x1>>y1>>x2>>y2;
		if(x2>maxx)
			maxx=x2;
		if(y2>maxy)
			maxy=y2;
		for(int i=x1;i<=x2;i++)
		{
			for(int j=y1;j<=y2;j++)
				mapb[i][j]=maps[i][j]=1;
		}
	}
}

bool check()
{
	for(int i=1;i<=maxx;i++)
		for(int j=1;j<=maxy;j++)
			if(maps[i][j])
				return true;
	return false;
}
void solve()
{
	int cnt=0;
	//cout<<maxx<<"  "<<maxy<<endl;
	while(check())
	{
		for(int i=1;i<=maxx;i++)
			for(int j=1;j<=maxy;j++){
			//	cout<<i<<" "<<j<<endl;
				if(!mapb[i-1][j] && !mapb[i][j-1])
					maps[i][j]=0;
				if(mapb[i-1][j] && mapb[i][j-1])
					maps[i][j]=1;
			}
			for(int i=1;i<=maxx;i++)
				for(int j=1;j<=maxy;j++){
					mapb[i][j]=maps[i][j];
				}
	cnt++;
	}
	cout<<cnt<<endl;
}
int main()
{
	freopen("out.txt","w",stdout);
	int cs;
	cin>>cs;
	for(int ii=1;ii<=cs;ii++)
	{
		cout<<"Case #"<<ii<<": ";
		init();
		solve();		
	}
	return 0;

}