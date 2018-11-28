#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
ifstream fin("A-large.in");
//ifstream fin("a.in");
ofstream fout("a.out");


const int d[4][2]={1,0,0,1,-1,0,0,-1};
int l;
vector<int> vert[6001];
vector<int> hori[6001];

bool ans[6001][6001];
int x0=3000, y0=3000;
int maxx, maxy, minx, miny;

void walk(int &x, int&y, int &dir, char s[])
{
	for (int i=0;s[i]!=0;i++)
	{
		if (s[i]=='F') 
		{
			if (dir==0)
				vert[x].push_back(y);
			else if (dir==2)
				vert[x-1].push_back(y);
			else if (dir ==1)
				hori[y].push_back(x);
			else hori[y-1].push_back(x);
			x+=d[dir][0];
			y+=d[dir][1];
			minx= min(x,minx);
			maxx=max(x,maxx);
			miny=min(y,miny);
			maxy=max(y,maxy);
		}
		else if (s[i]=='L')
			dir = (dir+3)%4;
		else dir = (dir+1)%4;
	}
}
void init()
{
	char s[100];
	int re;
	int x=x0, y=y0, dir=0;

	for (int i=0;i<6001;i++) hori[i].clear(), vert[i].clear();
	miny=maxy=minx=maxx=x0;
	fin>>l;
	for (int i=0;i<l;i++)
	{
		fin>>s>>re;
		for (int j=0;j<re;j++)
			walk(x,y,dir,s);
	}
}
void calc()
{
	memset(ans,0,sizeof(ans));
	for (int x=minx;x<maxx;x++)
		sort(vert[x].begin(),vert[x].end());
	for (int y=miny;y<maxy;y++)
		sort(hori[y].begin(),hori[y].end());

	for (int x=minx;x<maxx;x++)
		for (int i=1;i+1<vert[x].size();i+=2)
			for (int y=vert[x][i];y<vert[x][i+1];y++)
				ans[x][y]=true;
	for (int y=miny;y<maxy;y++)
		for (int i=1;i+1<hori[y].size();i+=2)
			for (int x=hori[y][i];x<hori[y][i+1];x++)
				ans[x][y]=true;
	int area = 0;
	for (int x=minx;x<maxx;x++)
		for (int y=miny;y<maxy;y++)
			if (ans[x][y]) area++;
	fout<<area<<endl;
}
int main()
{
	int t;
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		init();
		fout<<"Case #"<<i<<": ";
		calc();
		cout<<"~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
	}
	return 0;
}