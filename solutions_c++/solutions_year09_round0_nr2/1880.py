#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int h,w;
vector<vector<int> > altitudes(101);
vector<vector<int> > ret(101);
int cnt=0;

int dx[4]={0,-1,1,0};
int dy[4]={-1,0,0,1};

pair<int,int> lowest(int y, int x)
{
	int lowest=altitudes[y][x];
	int lowesti=-1;
	for(int i=0;i<4;i++)
	{
		int ny=y+dy[i];
		int nx=x+dx[i];
		if(ny<0||ny>=h) continue;
		if(nx<0||nx>=w) continue;
		if(lowest>altitudes[ny][nx])
		{
			lowest=altitudes[ny][nx];
			lowesti=i;
		}
	}
	return make_pair(lowest,lowesti);
}

void dfsflow(int y, int x)
{
	ret[y][x]=cnt;
	for(int i=0;i<4;i++)
	{
		int ny=y+dy[i];
		int nx=x+dx[i];
		if(ny<0||ny>=h) continue;
		if(nx<0||nx>=w) continue;
		pair<int,int> l=lowest(ny,nx);
		if(l.second>=0)
		{
			if(ny+dy[l.second] == y && nx+dx[l.second] == x)
				dfsflow(ny, nx);
		}
	}
}

void dfs(int y, int x)
{
	ret[y][x]=cnt;
	pair<int,int> l=lowest(y,x);
	if(l.first < altitudes[y][x])
	{
		dfs(y+dy[l.second],x+dx[l.second]);
	}
	else
	{
		dfsflow(y,x);
	}
}

int main()
{
	int TestCase;
	cin >> TestCase;
	for(int casei=0;casei<TestCase;casei++)
	{
		cnt=0;
		cin >> h >> w ;
		for(int i=0;i<h;i++)
		{
			altitudes[i].resize(w);
			ret[i].resize(w);
			for(int j=0;j<w;j++)
				cin >> altitudes[i][j];
		}

		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				ret[i][j]=-1;

		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				if(ret[i][j]==-1)
				{
					dfs(i,j);
					cnt++;
				}

		cout << "Case #"<<casei+1<<":"<<endl;
		for(int i=0;i<h;i++)
		{			
			for(int j=0;j<w;j++)
			{
				cout << (char)(ret[i][j]+'a') << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
