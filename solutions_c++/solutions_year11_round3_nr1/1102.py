#include <iostream>

using namespace std;

const int maxn = 52;
char matrix[maxn][maxn];
int r,c;

bool solve()
{
	int i , j ;
	for( i = 1 ; i <= r ; i++)
	{
		for ( j = 1 ; j <= c ; j++)
		{
			if(matrix[i][j]=='#')
			{
				if(i<r&&j<c&&matrix[i][j+1]=='#'&&matrix[i+1][j]=='#'&&matrix[i+1][j+1]=='#')
				{
					matrix[i][j] = matrix[i+1][j+1] = '/';
					matrix[i+1][j] = matrix[i][j+1] = '\\';
				}
				else return false ;
			}
		}
	}
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t , i , j , k ;
	cin>>t;
	for( i = 1 ; i <= t ; i++)
	{
		cin>>r>>c;
		for( j = 1 ; j <= r ; j++)
		{
			getchar();
			for( k = 1 ; k <= c ; k++)	cin>>matrix[j][k];
		}
		cout<<"Case #"<<i<<": "<<endl;
		if(solve())
		{
			for( j = 1 ; j <= r ; j++)
			{
				for( k = 1 ; k <= c ; k++)
				{
					cout<<matrix[j][k];
				}
				cout<<endl;
			}
		}
		else cout<<"Impossible"<<endl;
	}
	return 0;
}