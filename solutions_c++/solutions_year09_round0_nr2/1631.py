#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
int h,w,map[101][101],vis[101][101];

bool sink(int i, int j, int xl, int yl)
{
	int n=20000,we=20000,e=20000,s=20000,m=20000;

	if(i>0)	n=map[i-1][j];
	if(i<h-1)	s=map[i+1][j];
	if(j>0)	we=map[i][j-1];
	if(j<w-1)	e=map[i][j+1];

	m=min(n,we);
	m=min(m,e);
	m=min(m,s);

	if(m<map[i][j])
	{
		if(m==n)
		{
			if(xl==i-1 && yl==j)
				return true;
			return false;
		}
		if(m==we)
		{
			if(xl==i && yl==j-1)
				return true;
			return false;
		}
		if(m==e)
		{
			if(xl==i && yl==j+1)
				return true;
			return false;
		}
		if(m==s)
		{
			if(xl==i+1 && yl==j)
				return true;
			return false;
		}
	}

	return false;
}

void solve(int i, int j)
{
	if(i>=h || j>=w)
		return;
	if(vis[i][j]!=-1)
		return;
	vis[i][j]=-2;

	if(sink(i,j,i-1,j))
		solve(i-1,j);
	else if(sink(i,j,i,j-1))
		solve(i,j-1);
	else if(sink(i,j,i,j+1))
		solve(i,j+1);
	else if(sink(i,j,i+1,j))
		solve(i+1,j);
	if(sink(i+1,j,i,j))
		solve(i+1,j);
	if(sink(i,j+1,i,j))
		solve(i,j+1);
	if(sink(i,j-1,i,j))
		solve(i,j-1);
	if(sink(i-1,j,i,j))
		solve(i-1,j);
	
	return;
}

int main()
{
	freopen("bl.in","r",stdin);
	freopen("bl.out","w",stdout);
	int t;
	cin>>t;
	for(int tt=0;tt<t;tt++)
	{
		cin>>h>>w;
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				cin>>map[i][j];
		memset(vis,-1,sizeof(vis));
		int cnt=0;
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				if(vis[i][j]==-1)
				{
					solve(i,j);
					for(int a=0;a<h;a++)
					{
						for(int b=0;b<w;b++)
							if(vis[a][b]==-2)
								vis[a][b]=cnt;
					}
					cnt++;
				}
			}
		}
		cout<<"Case #"<<tt+1<<":\n";
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				if(j!=0)
					cout<<" ";
				cout<<char(vis[i][j]+'a');
			}
			cout<<endl;
		}
	}
	return 0;
}