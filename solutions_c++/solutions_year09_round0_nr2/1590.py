#include <iostream>

using namespace std;

int dir[4][2] = {-1,0,0,-1,0,1,1,0};
int n, m;
int a[100][100];
int ans[100][100];
int path[10000][2], len;
int letter;

void init()
{
	cin>>n>>m;
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			cin>>a[i][j];
}
void insert(int x, int y)
{
	path[len][0] = x;
	path[len][1] = y;
	len++;
}
void color(int c)
{
	for (int i=0; i<len;i++)
		ans[path[i][0]][path[i][1]] = c;
}
void search(int x, int y)
{
	int xx, yy, h, nextx, nexty;
	while (1)
	{
		insert(x,y);
		if (ans[x][y]>=0) break;
		h = a[x][y];
		for (int i = 0; i<4; i++)
		{
			xx=x+dir[i][0];
			yy=y+dir[i][1];
			if (xx>=0 && xx<n &&yy>=0 && yy<m)
				if (a[xx][yy]<h)
				{
					h = a[xx][yy];
					nextx = xx;
					nexty = yy;
				}
		}
		if (h<a[x][y])
		{
			x = nextx; y = nexty;
		}
		else break;
	}
	if (ans[x][y]>=0) color(ans[x][y]);
	else color(letter++);
}
void calc()
{
	memset(ans,-1,sizeof(ans));
	letter = 0;
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			if (ans[i][j]==-1)
			{
				len = 0;
				search(i,j);
			}
	for (int i=0;i<n;i++)
		for (int j=0; j<m;j++)
		{
			cout<<(char)(ans[i][j]+'a');
			if (j<m-1) cout<<' ';
			else cout<<endl;
		}
		
	
}
int main()
{
	int t;
	cin>>t;
	for (int i=0;i<t;i++)
	{
		init();
		cout<<"Case #"<<i+1<<":\n";
		calc();
	}
	return 0;
}
