#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstring>
#include<ctime>
#include<cstdlib>
using namespace std;

char a[60][60]={{0}};
void clean()
{
	for(int i = 1; i<=55; i++)
		for(int j = 1; j<=55; j++)
			a[i][j] = 0;
}
int main()
{
	
	//freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int i, j, k, ii, n, m, tt;
	bool fl;
	cin>>tt;
	for(ii = 1; ii<=tt; ii++)
	{
		cin>>n>>m;
		for(i = 1; i<=n; i++)
			for(j = 1; j<=m; j++)
				cin>>a[i][j];
		fl = 1;
		for(i = 1; i<=n; i++)
		{
			for(j = 1; j<=m; j++)
			{
				if(a[i][j]=='#')
				{
					if(a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#')
					{
						a[i][j+1] = a[i+1][j] = '\\';
						a[i][j] = a[i+1][j+1] = '/'; 
					}
					else
						fl = 0;
				}
				if(!fl)
					break;
			}
			if(!fl)
					break;
		}
		cout<<"Case #"<<ii<<":\n";
		if(!fl)
			cout<<"Impossible\n";
		else
		{
			for(i = 1; i<=n; i++)
			{
				for(j = 1; j<=m; j++)
					cout<<a[i][j];
				cout<<'\n';
			}
		}
		clean();
	}
	return 0;
}