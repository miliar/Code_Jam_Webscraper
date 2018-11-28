#include <iostream>
          
using namespace std;

const int dx[4] = {-1,0,0,1};
const int dy[4] = {0,-1,1,0};
int a[101][101],b[101][101];          
int n,m,i,j,t,k;

int dfs(int i,int j)
{
	if (b[i][j]>0) return b[i][j];
	int k,x,y,xx,yy;
	xx = 0;
	yy = 0;
	int p = 0;
	for (k = 0;k<=3;k++)
	{
		x = i+dx[k];
		y = j+dy[k];
		if ((x>=1)&&(x<=n)&&(y>=1)&&(y<=m)&&(a[x][y]<a[i][j])) 
		{
		//	p = max(p,dfs(x,y));
		//	break;	
		if ((xx == 0)||(a[xx][yy]>a[x][y]))
		{
			xx = x;
			yy = y;
		}
		}	
	}	
	if (xx>0) p = max(p,dfs(xx,yy));
	return p;
}

void solve(int i,int j)
{
	int k,x,y,xx,yy;
	b[i][j] = t;
	xx = 0;
	yy = 0;
	int p = 0;
	for (k = 0;k<=3;k++)
	{
		x = i+dx[k];
		y = j+dy[k];
		if ((x>=1)&&(x<=n)&&(y>=1)&&(y<=m)&&(a[x][y]<a[i][j])) 
		{
		//	p = max(p,dfs(x,y));
		//	break;	
		if ((xx == 0)||(a[xx][yy]>a[x][y]))
		{
			xx = x;
			yy = y;
		}
		}	
	}
	if (xx>0) solve(xx,yy);	
}




int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int w;
	cin >> w;
	for (int v= 1;v<=w;v++)
	{
		cin >> n >> m;
		for (i = 1;i<=n;i++)
			for (j = 1;j<=m;j++)
				cin >> a[i][j];
		memset(b,0,sizeof(b));
		k = 0;
		for (i = 1;i<=n;i++)
			for (j = 1;j<=m;j++)
			if (b[i][j] == 0)
			{
				int p = dfs(i,j);
			//	cerr << i <<  " " << j << " " << p << endl;
				if (p == 0) 
				{
					k++;
					t = k;
				}	
				else t = p;
				solve(i,j);	
			}
	   cout << "Case #" << v << ": " << endl;
	   for (i = 1;i<=n;i++)
	   {
	   	for (j = 1;j<=m;j++)
	   		cout << char(b[i][j]+96) << " ";
	   cout << endl;	
	   } 
	}
	return 0;
}




                       