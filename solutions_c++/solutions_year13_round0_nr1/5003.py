#include <iostream>
#include <stdlib.h>
#include <map>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <cmath>
using namespace std;


int main()
{
	freopen("in1.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 
	int t;
	cin >> t;
	for(int step = 1; step <= t; ++step)
	{
		vector<string> v(4);
		for(int i = 0; i < 4; ++i)
			cin >> v[i];
		bool Owin = false, Xwin=false, Dwin = false;

		for(int i = 0; i < 4; ++i)
		{
			bool O = true, X = true;
			for(int j = 0; j < 4; ++j)
				if(v[i][j] == '.')
					O = false, X = false, Dwin = true;
				else if(v[i][j] == 'X')
					O = false;
				else if (v[i][j] == 'O')
					X = false;
			Owin = Owin | O;
			Xwin = Xwin | X;
		}
		for(int j = 0; j < 4; ++j)
		{
			bool O = true, X = true;
			for(int i = 0; i < 4; ++i)
				if(v[i][j] == '.')
					O = false, X = false, Dwin = true;
				else if(v[i][j] == 'X')
					O = false;
				else if (v[i][j] == 'O')
					X = false;
			Owin = Owin | O;
			Xwin = Xwin | X;
		}
		bool O = true, X = true;
		for(int i = 0; i < 4; ++i)
		{						
				if(v[i][i] == '.')
					O = false, X = false, Dwin = true;
				else if(v[i][i] == 'X')
					O = false;
				else if (v[i][i] == 'O')
					X = false;			
		}
		Owin = Owin | O;
		Xwin = Xwin | X;
		O = true, X = true;
		for(int i = 0; i < 4; ++i)
		{		
				if(v[i][3-i] == '.')
					O = false, X = false, Dwin = true;
				else if(v[i][3-i] == 'X')
					O = false;
				else if (v[i][3-i] == 'O')
					X = false;
		}
		Owin = Owin | O;
		Xwin = Xwin | X;
		printf("Case #%d: ", step);
		if(Owin)
			cout << "O won" << endl;
		else if(Xwin)
			cout << "X won" << endl;
		else if (Dwin)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" <<endl;
	}
}