#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <limits>
using namespace std;

int main(void) {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{		
		int R, C;

		cin >> R;		
		cin >> C;

		char titles[50][50]; 	
		bool possible = true;

		for (int j = 0; j < R; j++)
		{	
			int count = 0;
			for (int k = 0; k < C; k++)
			{
				cin >> titles[j][k];				
				if (titles[j][k] == '#') count++;			
			}				
			if ((count % 2) != 0) 
			{
				possible = false;								
			}
		}

		if (possible) 
		{
			for (int j=0; j < (R - 1); j++)
			{
			
				for (int k = 0; k < (C - 1); k++)
				{
					if ((titles[j][k] == '#' && titles[j][k+1] == '#') &&
						(titles[j+1][k] == '#' && titles[j+1][k+1] == '#'))
					{
						titles[j][k]   = '/';	titles[j][k+1]	 = '\\';
						titles[j+1][k] = '\\';	titles[j+1][k+1] = '/';
					}
				}							
			}
		}

		for (int j = 0; j < R; j++)
		{	
			for (int k = 0; k < C; k++)
			{
				if (titles[j][k] == '#') possible = false;
			}	
		}

		cout << "Case #" << (i+1) << ":\n";
		
		if (!possible) 
		{
			cout <<"Impossible\n";
		} else 
		{			
			for (int j = 0; j < R; j++)
			{	
				int count = 0;
				for (int k = 0; k < C; k++)
				{
					cout << titles[j][k];
				}			
				cout << "\n";
			}
		}
	}
}
