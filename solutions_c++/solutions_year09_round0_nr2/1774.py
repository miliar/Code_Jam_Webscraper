#include<iostream>
#include<fstream>
using namespace std;

int dx[]={0,-1,0,0,1};
int dy[]={0,0,-1,1,0};
int map[101][101],z;
int h[101][101];
int n,m;

bool able(int x,int y)
{
	if(1<=x && x<=n)
		if(1<=y && y<=m)
			return true;
	return false;
}

void doit(int x,int y)
{
	if(map[x][y])
		return;
	int lowest=10001,d=0;
	for(int i=1;i<=4;i++)
		if(able(x+dx[i],y+dy[i]))
			if(h[x+dx[i]][y+dy[i]] < h[x][y])
				if(h[x+dx[i]][y+dy[i]] < lowest)
					lowest=h[x+dx[i]][y+dy[i]],d=i;
	if(d == 0)
		map[x][y] = ++z;
	else
	{
		doit(x+dx[d],y+dy[d]);
		map[x][y] = map[x+dx[d]][y+dy[d]] ;
	}
	return ;
}

int chr[101];
int zc;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int T;
	cin>>T;
	for(int c=1;c<=T;c++)
	{
		memset(map,0,sizeof(map));
		memset(chr,0,sizeof(chr));
		z=0;
		zc=0;
		cin>>n>>m;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				cin>>h[i][j];
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				if(!map[i][j])
					doit(i,j);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				if(chr[map[i][j]] == 0)
					chr[map[i][j]]=++zc;
		cout<<"Case #"<<c<<":"<<endl;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
			{
				cout<<char('a'+chr[map[i][j]]-1);
				if(j<m)
					cout<<" ";
				else
					cout<<endl;
			}
	}
	return 0;
}
