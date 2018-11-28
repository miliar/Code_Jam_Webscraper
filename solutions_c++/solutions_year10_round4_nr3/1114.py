#include <iostream>
#include <vector>

using namespace std;
#define sz 101

bool has(int mat[sz][sz])
{
	for(int i = 1; i < sz; i++)
		for(int j = 1; j < sz; j++)
		{
			if (mat[i][j] == 1) return true;
		}
	return false;
}

int main()
{
	int cases;
	int c = 1;
	cin >> cases;
	while (cases-- > 0)
	{
		int r;
		int x1, y1, x2, y2;
		int mat[sz][sz];
		cin >> r;
		for(int i = 0; i < sz; i++)
			for(int j = 0; j < sz; j++)
			{
				mat[i][j] = 0;
			}
		while (r-- > 0)
		{
			cin >> x1 >> y1 >> x2 >> y2;
			for(int i = x1; i <= x2; i++)
			{
				for(int j = y1; j <= y2; j++)
				{
					mat[j][i] = 1;
				}
			}			
			
		}/*
		for(int i = 0; i < sz; i++)
		{
			for(int j = 0; j < sz; j++)
			{
				cout << mat[j][i] << " ";
			}
			cout << endl;
		}
*/		
		
		int rounds = 0;
		while (has(mat))
		{
			for(int i = sz-1; i > 0; i--)
			{
				for(int j = sz-1; j > 0; j--)
				{
					if (mat[i][j] == 1)
					{
						if (mat[i-1][j] == 0 && mat[i][j-1] == 0)
						{
							mat[i][j] = 0;
						}
					}
					else
					{
						if (mat[i-1][j] == 1 && mat[i][j-1] == 1)
						{
							mat[i][j] = 1;
						}
					}
				}
			}/*
			cout << endl;
			for(int i = 0; i < sz; i++)
			{
				for(int j = 0; j < sz; j++)
				{
					cout << mat[j][i] << " ";
				}
				cout << endl;
			}*/
			
			rounds++;
		}
		
		cout << "Case #" << c++ <<": " << rounds << endl;
		
	}
	
}