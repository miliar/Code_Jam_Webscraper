#include <iostream>

using namespace std;

int a[105][105],x,y,b[105][105];

int dfs(int p,int	q)
{
	if (b[p][q]!=-1)
		return b[p][q];
	int u=a[p][q];
	u=min(u,a[p-1][q]);
	u=min(u,a[p+1][q]);
	u=min(u,a[p][q-1]);
	u=min(u,a[p][q+1]);
	if (u==a[p][q])
	{
		b[p][q]=p*1000+q;
		return b[p][q];
	}
	if (u==a[p-1][q])
		b[p][q]=dfs(p-1,q);
	else if (u==a[p][q-1])
		b[p][q]=dfs(p,q-1);
	else if (u==a[p][q+1])
		b[p][q]=dfs(p,q+1);
	else if (u==a[p+1][q])
		b[p][q]=dfs(p+1,q);
	return b[p][q];
}

int main()
{
	int n;
	cin>>n;
	for (int m=1;m<=n;m++)
	{
		cout<<"Case #"<<m<<":\n";		
		cin>>x>>y;
		for (int i=0;i<105;i++)
			for (int j=0;j<105;j++)
				a[i][j]=99999;
		for (int i=1;i<=x;i++)
			for (int j=1;j<=y;j++)
				cin>>a[i][j],b[i][j]=-1;
		for (int i=1;i<=x;i++)
			for (int j=1;j<=y;j++)
				dfs(i,j);
		int v=0;
		int s[30];
		for (int i=1;i<=x;i++)
		{
			for (int j=1;j<y;j++)
			{
				bool xd=1;
				for (int k=0;k<v;k++)
					if (s[k]==b[i][j])
						cout<<(char)(k+'a')<<' ',xd=0;
				if (xd)
				{
					s[v]=b[i][j];
					cout<<(char)(v+'a')<<' ';
					v++;
				}
			}
			int j=y;
			bool xd=1;
			for (int k=0;k<v;k++)
				if (s[k]==b[i][j])
					cout<<(char)(k+'a')<<' ',xd=0;
			if (xd)
			{
				s[v]=b[i][j];
				cout<<(char)(v+'a')<<' ';
				v++;
			}
			cout<<endl;
		}
	}
	return 0;
}