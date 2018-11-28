#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	int TC;cin>>TC;
	for ( int k=0; k <TC; k++ ){
	int R;
	int C;
	cin>>R;cin>>C;
	char A[R][C];
	for ( int i=0; i<R; i++ )
	for ( int j=0; j<C; j++ )
	cin>>A[i][j];
	bool r = true;
	bool c = true;
	for ( int i=0; i<R; i++ )
	{
		for ( int j=0; j<C; j++ )
		{
			//if ( ( i+1 < R)&&( j+1 < C ) )
			//{
				if ( ( A[i][j] == '#' ) )
				{
					if ( ( i+1 < R)&&( j+1 < C ) ){
					if ( ( A[i][j+1] == '#') && ( A[i+1][j] =='#' ) && ( A[i+1][j+1] == '#' ) )
					{
						A[i][j]   = '/';
						A[i][j+1] = '\\';
						A[i+1][j]   = '\\';
						A[i+1][j+1] = '/';
						c = true;
					}else c = false;}else c = false;
				}
			//}
			if ( !c )
			{
				r = false;
				break;
			}
		}if ( !r )
		break;
	}
	if ( r )
	{
		cout<<"Case #"<<k+1<<":\n";
		for ( int i=0; i<R; i++ )
		{
			for ( int j=0; j<C; j++ )
			cout<<A[i][j];
			cout<<endl;
		}
	}else cout<<"Case #"<<k+1<<":\n"<<"Impossible\n";
	}
	return 0;
}
