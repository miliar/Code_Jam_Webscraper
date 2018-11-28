#include <iostream>

using namespace std;

/*
void dispGrid(int grid[][101], int mx, int my)
{
	cout << endl;
	for(int i=1; i<=mx; ++i)
	{
		for(int j=1; j<=my; ++j)
			cout << grid[i][j];
		cout << endl;
	}
}
*/

int main()
{
	int T, maxx, maxy, R, X1, X2, Y1, Y2, count, s;
	cin >> T;
	int Grid[101][101];
	for(int t=1; t<=T; ++t)
	{
		maxx = 0; maxy=0;
		for(int i=0; i<101; ++i)
			for(int j=0; j<101; ++j)
			{
				Grid[i][j] = 0;
			}
		cout << "Case #" << t << ": ";
		cin >> R;
		for(int r=0; r<R; ++r)
		{
			cin >> X1 >> Y1 >> X2 >> Y2;
			if(X2 > maxx)
				maxx = X2;
			if(Y2 > maxy)
				maxy = Y2;
			count = 0;
			for(int i=X1; i<=X2; ++i)
				for(int j=Y1; j<=Y2; ++j)
				{
					Grid[j][i] = 1;
					++count;
				}
		}
		s=0;
		while(count)
		{
			count = 0;
			++s;
			for(int i=maxx; i; --i)
				for(int j=maxy; j; --j)
				{
					Grid[j][i] = (Grid[j-1][i] & Grid[j][i-1]) | (Grid[j][i] & (Grid[j-1][i] | Grid[j][i-1]));
					count += Grid[j][i];
				}

		}
		cout << s << endl;
	}
	return 0;
}
