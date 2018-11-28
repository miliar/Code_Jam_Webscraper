#include <cstdio>
#include <iostream>
using namespace std;




void mos(int t)
{
	char tabla[52][52];
	int r,c;
	int i,j;
	cin >> r >> c;
	for ( i = 0 ; i < r ; i++ )
		cin >> tabla[i];
	
	int blue = 0;
	for ( i = 0 ; i < r ; i++ )
		for ( j = 0 ; j < c ; j++ )	
			if ( tabla[i][j] == '#' )
				blue++;
	cout << "Case #"<< t << ":" << endl;
	if ( blue % 4 )
	{
		cout << "Impossible" << endl;
		return;
	}
	
	for ( i = 0 ; i < r ; i++ )
		for ( j = 0 ; j < c ; j++ )
		{
			if ( tabla[i][j] == '#' )
			{
				if ( tabla[i][j+1] == '#' &&
				     tabla[i+1][j] == '#' &&
					 tabla[i+1][j+1] == '#' )
				{
					tabla[i][j] = '/'; 
					tabla[i][j+1] = '\\'; 
				    tabla[i+1][j] = '\\'; 
					tabla[i+1][j+1] = '/';	
				}				
				else
				{					
					cout << "Impossible" << endl;
					return;
				}
			}
		}
	
	for ( i = 0 ; i < r ; i++ )
		cout << tabla[i] << endl;
}

int main()
{
	int t;
	cin >> t;
	int i;
	for ( i = 1 ; i <= t ; i++ )
	{
		mos(i);
	}	
	return 0;
}