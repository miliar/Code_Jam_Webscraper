#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
	int T, R, C;
	char b_picture[50][50];
	char r_picture[50][50];
	bool flag = false;
	
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		cout << "Case #" << t << ":" << endl;
		cin >> R >> C;
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
			{
				cin >> b_picture[i][j];
				r_picture[i][j] = b_picture[i][j];
			}
		flag = false;
		
		for(int i=0; i<R; i++)
		{
			for(int j=0; j<C; j++)
			{
				if(b_picture[i][j] == '.')
					r_picture[i][j] = '.';
				else if(r_picture[i][j] == '/' || r_picture[i][j] == '\\')
					continue;
				else if(b_picture[i][j] == '#')
				{
					if(i == R-1 || j == C-1) flag = true;
					else if(b_picture[i+1][j] == '#' && b_picture[i][j+1] == '#' && b_picture[i+1][j+1] == '#')
					{
						r_picture[i][j] = '/';
						r_picture[i][j+1] = '\\';
						r_picture[i+1][j] = '\\';
						r_picture[i+1][j+1] = '/';
					}
					else 
					{
						flag = true;
						//~ cout << "Setou true" << endl;
					}
				}
			}
			//~ cout << "saiu do for" << endl;
			if(flag) break;
			//~ cout << "imprimiu isso" << endl;
		}
		if(!flag)
		{
			for(int i=0; i<R; i++)
			{
				for(int j=0; j<C; j++)
					cout << r_picture[i][j];
				cout << endl;
			}
		}
		else cout << "Impossible" << endl;
	}

	return 0;
}
