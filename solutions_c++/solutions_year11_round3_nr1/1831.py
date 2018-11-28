#include <iostream>

using namespace std;

int main()
{
	int TestCases;
	
	cin >> TestCases;
	
	for(int i=0;i < TestCases;i++)
	{
		int R,C;
		char Tiles[50][50];
		int flag=1;
		
		cin >> R >> C;	
		
		for(int j=0;j < R;j++)
		{
			for(int k=0;k < C;k++)
				cin >> Tiles[j][k];			
		}
		
		for(int j=0;j < R;j++)
		{
			for(int k=0;k < C;k++)
			{
				if( Tiles[j][k] == '#' )
				{
					if( (Tiles[j+1][k] != '#' || Tiles[j][k+1] != '#' || Tiles[j+1][k+1] != '#')  || (j == R-1 && k == C-1) )
						flag = 0;
						
					else
					{
						Tiles[j][k] = Tiles[j+1][k+1] = '/';
						Tiles[j+1][k] = Tiles[j][k+1] = '\\';
					}
				}
			}
		}
		
		cout << "Case #" << (i+1) << ": " << endl;
		
		if( flag == 1 )
		{
			for(int j=0;j < R;j++)
			{
				for(int k=0;k < C;k++)
					cout << Tiles[j][k];
				cout << endl;
			}
		}
		else
			cout << "Impossible\n";
	}
}
