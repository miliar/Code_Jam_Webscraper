#include <iostream>
#include <vector>
using namespace std;

int inf=9999999;

int min(int x, int y, int z)
{
	if (x<=y && x<=z)
		return x;
	if (y<=x && y<=z)
		return y;
	return z;
}

int main()
{
	int n,m,i,V;
	cin>>n;
	int t;
	for (t=1; t<=n; t++)
	{
		cin>>m>>V;
		vector<int> g(m+1);
		vector<int> c(m+1,0);
		vector<vector<int> > v(m+1, vector<int>(2));
		for (i=1; i<=(m-1)/2; i++)
		{
			cin>>g[i]>>c[i];
		}
		int x;
		for (; i<=m; i++)
		{
			cin>>x;
			v[i][x]=0;
			v[i][1-x]=inf;
		}
		for (i=(m-1)/2; i>=1; i--)
		{
			int l,r;
			l=2*i;
			r=2*i+1;
			if (g[i]==1)
			{
				//AND
				v[i][0]=min(v[l][0]+v[r][0], v[l][0]+v[r][1], v[l][1]+v[r][0]);
				v[i][1]=v[l][1]+v[r][1];
			}
			else
			{
				//OR
				v[i][1]=min(v[l][1]+v[r][1], v[l][0]+v[r][1], v[l][1]+v[r][0]);
				v[i][0]=v[l][0]+v[r][0];
			}
			if (c[i]==1)
			{
				if (g[i]==0)
				{
					// switch to AND
					int y;
					y=min(v[l][0]+v[r][0], v[l][0]+v[r][1], v[l][1]+v[r][0]);
					if (v[i][0]>y+1)
						v[i][0]=y+1;
					y=v[l][1]+v[r][1];
					if (v[i][1]>y+1)
						v[i][1]=y+1;
				}
				else
				{
					// switch to OR
					int y;
					y=min(v[l][1]+v[r][1], v[l][0]+v[r][1], v[l][1]+v[r][0]);
					if (v[i][1]>y+1)
						v[i][1]=y+1;
					y=v[l][0]+v[r][0];
					if (v[i][0]>y+1)
						v[i][1]=y+1;
				}
			}
		}
		if (v[1][V]!=inf)
			cout<<"Case #"<<t<<": "<<v[1][V]<<endl;
		else
			cout<<"Case #"<<t<<": IMPOSSIBLE\n";
	}
	return 0;
}
