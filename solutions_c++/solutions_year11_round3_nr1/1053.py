#include <iostream>

using namespace std;

int main ()
{
	int T, R, C;
	cin >> T;
	for (int i=0;i<T;++i)
	{
		cin >> R >> C;
		char GRID[R][C];
		int blueTiles;
		cout << "Case #" << i+1 << ":" << endl;
		for (int j=0;j<R;++j)
			for (int k=0;k<C;++k)
				cin >> GRID[j][k];
				
		bool imp=false;
		for (int j=0;j<R;++j)
		{
			blueTiles=0;
			for (int k=0;k<C;++k)
			{
				if (GRID[j][k] == '#')
					++blueTiles;
			}
			if (blueTiles%2!=0){
				cout << "Impossible" << endl;
				imp=true;
				break;
			}
		}
		
		if (imp==false) //continue
		{
		for (int j=0;j<R;++j)
		{
			for (int k=0;k<C;++k)
			{
				if (GRID[j][k] == '#')
				{
					if (GRID[j][k+1]=='#' && GRID[j+1][k+1]=='#' && GRID[j+1][k]=='#')
					{
						GRID[j][k]='/';
						GRID[j][k+1]='\\';
						GRID[j+1][k]='\\';
						GRID[j+1][k+1]='/';
					}
					else
					{
						cout << "Impossible" << endl;
						imp=true;
						break;
					}
				}
			}
			if (imp==true)
				break;
		}			
		}
		if (imp==false)
		{
			for (int j=0;j<R;++j){
				for (int k=0;k<C;++k){
					cout << GRID[j][k];
				}
				cout << endl;
			}
		}

		
	}
}
