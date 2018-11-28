#include <iostream>
#include <map>
using namespace std;
int mat[100][100];
int next[100][100];
char ret[100][100];
int m, n;
char lab;
int dx[]={-1,0,0,1}, dy[]={0,-1,1,0};
int dir(int d)
{
	if(d==0) return 3;
	if(d==3) return 0;
	if(d==1) return 2;
	if(d==2) return 1;
}
bool inside(int x, int y)
{
	return (x>=0 && x<m && y>=0 && y<n);
} 
void check(int x, int y)
{
	int hmin=10000000, imin, ix, iy;
	for(int i=0; i<4; i++)
	{
		ix = x+dx[i], iy = y+dy[i];
		if(inside(ix, iy))
			if(mat[ix][iy]<hmin)
			{
				hmin = mat[ix][iy];
				imin = i;	
			}
	}
	if(hmin >= mat[x][y]) next[x][y] = -1;
	else next[x][y] = imin;
}
void dfs(int x, int y)
{
	if(!inside(x, y)) return;
	int i, ix, iy;
	ret[x][y] = lab;
	for(i=0; i<4; i++)
	{
		ix = x+dx[i], iy = y+dy[i];
		if(inside(ix, iy))
			if(next[ix][iy] == dir(i)) dfs(ix, iy);
	}
}
void show()
{
	int i, j;
	for(i=0; i<m; i++)
	{
		for(j=0; j<n-1; j++)
			cout << ret[i][j] << ' ';
		cout << ret[i][j] << endl;
	}
}
int main()
{
	int t, h, i, j, k=0;
	char tmp;
	cin >> t;
	
	while(t--)
	{
		memset(ret, 0, sizeof(ret));
		cin >> m >> n;
		for(i=0; i<m; i++)
			for(j=0; j<n; j++)
				cin >> mat[i][j];
		for(i=0; i<m; i++)
			for(j=0; j<n; j++)
				check(i, j);
		lab = 'a';
		for(i=0; i<m; i++)
			for(j=0; j<n; j++)
				if(next[i][j]==-1)
				{
					ret[i][j] = lab;
					dfs(i, j);
					lab++;
				}
		map<char, char> dist;
		lab = 'a';
		for(i=0; i<m; i++)
			for(j=0; j<n; j++)
			{
				tmp = dist[ret[i][j]];
				if(!tmp)
				{
					dist[ret[i][j]] = lab; 
					ret[i][j] = lab;
					lab++;
				}
				else
				{
					ret[i][j] = tmp;
				}
			}
		printf("Case #%d:\n", ++k);
		show();
	}
}
