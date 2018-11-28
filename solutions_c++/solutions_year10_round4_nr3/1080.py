#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <conio.h>
#include <boost/format.hpp>
using namespace std;
using namespace boost;

const int SZ=101;

bool isNoBacterium(int map[SZ][SZ])
{
	for(int y=1;y<SZ;y++)
	for(int x=1;x<SZ;x++)
	{
		if(map[y][x]==1)
			return false;
	}
	return true;
}

void print(int map[SZ][SZ])
{
	for(int y=0;y<8;y++)
	{
		for(int x=0;x<8;x++)
			cerr<<map[y][x];
		cerr<<endl;
	}
}

int solve()
{
	int R; cin>>R;
	
	int map[SZ][SZ]={0};
	for(int i=0;i<R;i++)
	{
		int x1,y1,x2,y2; cin>>x1>>y1>>x2>>y2;
		//cerr<<format("(%d,%d)-(%d,%d)")%x1%y1%x2%y2<<endl;
		for(int y=y1;y<=y2;y++)
		for(int x=x1;x<=x2;x++)
			map[y][x]=1;
	}
	
	for(int s=1;s<SZ*SZ;s++)
	{
		//cerr<<format("[%d]")%s<<endl;
		//print(map);
		
		for(int y=SZ-1;y>=0;y--)
		for(int x=SZ-1;x>=0;x--)
		{
			if(map[y  ][x-1]==0 && map[y-1][x  ]==0)
				map[y][x]=0;
			if(map[y][x]==0)
				if(map[y  ][x-1]==1 && map[y-1][x  ]==1)
					map[y][x]=1;
		}
		
		if(isNoBacterium(map)==true)
			return s;
	}
	assert(false);
	return -1;
}

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		int ans=solve();
		cout<<format("Case #%d: %d")%ds%ans<<endl;
	}
	return 0;
}
