#include <iostream>
using namespace std;
int m,n;
char mat[100][100];
int solve()
{
	int i,j;
	for(i=0;i<n;++i)
	{
		for(j=0;j<m;++j)
		{
			if(mat[i][j]=='#')
			{
				if(i==n-1 || j==m-1)
					return 0;
				if((mat[i+1][j]=='#')&&(mat[i][j+1]=='#')&&(mat[i+1][j+1]=='#'))
				{
					mat[i][j]='/';
					mat[i][j+1]='\\';
					mat[i+1][j]='\\';
					mat[i+1][j+1]='/';
				}
				else
				{
					return 0;
				}
			}
		
		}
	}
	return 1;
}

int main()
{
	int T,j,i,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	for(i=1;i<=T;++i)
	{
		cin>>n>>m;
		for(j=0;j<n;++j)
		{
			for(k=0;k<m;++k)
			{
				cin>>mat[j][k];
			}
		}
		if(!solve())
		{
			cout<<"Case #"<<i<<":"<<endl;
			cout<<"Impossible"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<":"<<endl;
			for(j=0;j<n;++j)
			{
				for(k=0;k<m;++k)
				{
					cout<<mat[j][k];
				}
				cout<<endl;
			}
		}
	}
	return 0;
}