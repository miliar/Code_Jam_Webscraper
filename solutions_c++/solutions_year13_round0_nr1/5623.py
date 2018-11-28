#include <iostream>
#include <string>
using namespace std;

int Xrow[4];
int Xcol[4];
int Xdiag[2];
int Ocol[4];
int Orow[4];
int Odiag[2];
int draw = 1;
int win;

int main()
{
	ios_base::sync_with_stdio(0);
	
	int N;
	cin >> N;
	
	for( int i = 0; i < N; i++ )
	{
		
		draw = 1;
		win = 0;
		
		for( int c = 0; c < 4; c++ )
		{	
			Xrow[c]=0;
			Xcol[c]=0;
			Xdiag[c]=0;
			Ocol[c]=0;
			Orow[c]=0;
			Odiag[c]=0;
		}
		
		for( int y = 0; y < 4; y++ )
		{
			char line[5];
			cin >> line;
			for( int x = 0; x < 4; x++ )
			{					
				if( line[x] == 'X' || line[x] == 'T' )
				{
					Xrow[y]++;
					Xcol[x]++;
					if( x == y )
						Xdiag[0]++;
					if( x + y == 3 )
						Xdiag[1]++;
				}
				
				if( line[x] == 'O' || line[x] == 'T' )
				{
					Orow[y]++;
					Ocol[x]++;
					if( x == y )
						Odiag[0]++;
					if( x+y == 3 )
						Odiag[1]++;
				}
				
				if( line[x] == '.' )
				{
					draw = 0;
				}
			}
		}
		
		cout << "Case #"<< i+1 <<": ";
		
		//cout << "sprawdzam draw: " << draw<< "\n";
		
		for( int w = 0; w < 4; w++ )
		{
			if( Xrow[w] == 4 || Xcol[w] == 4 )
			{
				cout << "X won";
				win = true;
				break;
			}
			else
			if( Orow[w] == 4 || Ocol[w] == 4 )
			{
				cout << "O won";
				win = true;
				break;
			}
		}
		for( int w = 0; w < 2; w++ )
		{
			if( Xdiag[w] == 4 )
			{
				cout << "X won";
				win = true;
				break;
			}
			if( Odiag[w] == 4 )
			{
				cout << "O won";
				win = true;
				break;
			}
		}
		
		if( win == 0 )
		{
			if( draw == 1 )
				cout << "Draw";
			else
				cout << "Game has not completed";
		}
		cout << "\n";
	}
	
	return 0;
}
