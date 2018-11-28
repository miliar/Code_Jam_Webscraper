#include<iostream>
#include<cstring>
using namespace std;

const int Max = 100;
char map[Max][Max];
int flowto[Max][Max];
int height[Max][Max];
int h,w;
bool Range(int a,int b,int c){return a<=b && b<c;}
int calc(int x,int y);
bool target(int x,int y,int x2,int y2);
void BFS(int x,int y,char ch);
int main()
{
	int n,cases=0;
	cin>>n;
	while(n-- > 0)
	{
		cin>>h>>w;
		memset(map,0,sizeof(map));
		memset(flowto,0,sizeof(flowto));
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				cin>>height[i][j];
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				flowto[i][j] = calc(i,j);
		char ch = 'a';
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				if(map[i][j] == '\0')
					BFS(i,j,ch++);
		cout<<"Case #"<<++cases<<":\n";
		for(int i=0;i<h;i++,cout<<endl)
			for(int j=0;j<w;j++)
				cout<<map[i][j]<<' ';
	}
	return 0;
}
int calc(int x,int y)
{
	int a[4];
	const int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
	memset(a,0x7f,sizeof(a));
	for(int i=0;i<4;i++)
	{
		int x2 = x+dir[i][0], y2 = y+dir[i][1];
		if(Range(0,x2,h) && Range(0,y2,w))
			a[i] = height[x2][y2] - height[x][y];
	}
	int curmin = 0, z = -1;
	for(int i=0;i<4;i++)
		if(a[i] < curmin)
			curmin = a[i], z = i;
	if(z >= 0) return (x+dir[z][0])*w+(y+dir[z][1]);
	return -1;
}
bool target(int x,int y,int x2,int y2)
{
	int x3 = flowto[x][y]/w, y3 = flowto[x][y]%w;
	return x2 == x3 && y2 == y3;
}
int start,end;
int queue[Max*Max];
void BFS(int x,int y,char ch)
{
	start = end = 0;
	map[x][y] = ch;
	queue[end++] = x*w+y;
	while(start < end)
	{
		int t = queue[start++];
		x = t/w, y = t%w;
		int x2 = flowto[x][y]/w, y2 = flowto[x][y]%w;
		if(map[x2][y2] == '\0')
		{
			queue[end++] = x2*w+y2;
			map[x2][y2] = ch;
		}
		if(x > 0 && map[x-1][y] == '\0' && target(x-1,y,x,y))
		{
			queue[end++] = x*w+y-w;
			map[x-1][y] = ch;
		}
		if(x < h-1 && map[x+1][y] == '\0' && target(x+1,y,x,y))
		{
			queue[end++] = x*w+y+w;
			map[x+1][y] = ch;
		}
		if(y > 0 && map[x][y-1] == '\0' && target(x,y-1,x,y))
		{
			queue[end++] = x*w+y-1;
			map[x][y-1] = ch;
		}
		if(y < w-1 && map[x][y+1] == '\0' && target(x,y+1,x,y))
		{
			queue[end++] = x*w+y+1;
			map[x][y+1] = ch;
		}
	}
}
