#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	
	freopen("A-large.in", "r", stdin);
	freopen("largeoutA.txt", "w", stdout);
	
	int TC;
	cin >> TC;
	
	for(int k = 0; k < TC; ++k)
	{
		vector<string> GRID;
		bool inc = false;
		
		for(int u = 0; u < 4; ++u)
		{
			string S;
			cin >> S;
			
			if( S.find('.' ) != string::npos )
				inc = true;
			
			GRID.push_back(S);
		}
		
		bool ans = false;
		
		for(int i = 0; i < 4 && !ans; ++i)
		{
			for(int j = 0; j < 4 && !ans; ++j)
			{
				int sum_hor = 1;
				int sum_ver = 1;
				int sum_dia_princ = 1;
				int sum_dia_sec = 1;
				
				char c = GRID[i][j];
				
				if( c == '.' )
					continue;
				
				// sum_hor right
				for(int col = j + 1; col < 4; ++col)
					if( GRID[i][col] == c || GRID[i][col] == 'T' )
						sum_hor++;
					else
						break;
						
				// sum_hor left
				for(int col = j - 1; col >= 0; --col)
					if( GRID[i][col] == c || GRID[i][col] == 'T' )
						sum_hor++;
					else
						break;
						
				// sum_ver up
				for(int row = i - 1; row >= 0; --row)
					if( GRID[row][j] == c || GRID[row][j] == 'T' )
						sum_ver++;
					else
						break;
						
				// sum_ver down
				for(int row = i + 1; row < 4; ++row)
					if( GRID[row][j] == c || GRID[row][j] == 'T' )
						sum_ver++;
					else
						break;
						
				// sum_dia_princ down
				for(int row = i + 1, col = j + 1 ; row < 4 && col < 4; ++row, ++col)
					if( GRID[row][col] == c || GRID[row][col] == 'T' )
						sum_dia_princ++;
					else
						break;
						
				// sum_dia_princ up
				for(int row = i - 1, col = j - 1 ; row >= 0 && col >= 0; --row, --col)
					if( GRID[row][col] == c || GRID[row][col] == 'T' )
						sum_dia_princ++;
					else
						break;
						
				// sum_dia_sec down
				for(int row = i + 1, col = j - 1 ; row < 4 && col >= 0; ++row, --col)
					if( GRID[row][col] == c || GRID[row][col] == 'T' )
						sum_dia_sec++;
					else
						break;
						
				// sum_dia_sec up
				for(int row = i - 1, col = j + 1 ; row >= 0 && col < 4; --row, ++col)
					if( GRID[row][col] == c || GRID[row][col] == 'T' )
						sum_dia_sec++;
					else
						break;
				/*		
				cout << i << "," << j << endl << sum_hor << " " << sum_ver << " " << sum_dia_princ << " " << sum_dia_sec << endl;
				cin.get();
				cin.get();
				*/
						
				if( sum_hor == 4 || sum_ver == 4 || sum_dia_princ == 4 || sum_dia_sec == 4)
				{
					cout << "Case #" << k + 1 << ": " << c << " won" << endl;
					ans = true;
				}	
			}
		}
		
		if( ans == false )
		{
			if(inc)
				cout << "Case #" << k + 1 << ": " << "Game has not completed" << endl;
			else
				cout << "Case #" << k + 1 << ": " << "Draw" << endl;
		}
	}
	
	return 0;
}
