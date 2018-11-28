#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 110

const int dir[4][2]=
{
	-1,0,
	0,-1,
	0,1,
	1,0
};

int n,m;
int height[MAXN][MAXN];
int c;
int color[MAXN][MAXN];
char output[MAXN*MAXN];

int calc_color(int x,int y)
{
	int& ans=color[x][y];
	if (ans==-1)
	{
		int d=-1;
		int x1=x;
		int y1=y;
		int h=height[x][y];
		for (int i=0;i<4;i++)
		{
			int x2=x+dir[i][0];
			int y2=y+dir[i][1];
			if (height[x2][y2]<h)
			{
				x1=x2;
				y1=y2;
				d=i;
				h=height[x2][y2];
			}
		}
		if (d==-1) ans=c++;
		else ans=calc_color(x1,y1);
	}
	return ans;
}

int caseN;
int main()
{
	cin>>caseN;
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		cin>>n>>m;
		memset(height,127,sizeof(height));
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				cin>>height[i][j];
		c=0;
		memset(color,-1,sizeof(color));
		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=m;j++)
			{
				cerr<<calc_color(i,j)<<' ';
			}
			cerr<<endl;
		}
		memset(output,0,sizeof(output));
		cout<<"Case #"<<caseI<<":"<<endl;
		c='a';
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
			{
				if (!output[color[i][j]])
					output[color[i][j]]=c++;
				cout<<output[color[i][j]];
				if (j==m) cout<<endl;
				else cout<<' ';
			}
	}
	return 0;
}

