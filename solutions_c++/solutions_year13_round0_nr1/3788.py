#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
	ifstream cin ( "input.txt" );
	ofstream cout ( "output.txt" );
	int t;
	cin >> t;
	int all = t;
	while (t--)
	{
		cin >> ws;
		bool flag = false;
		bool flag1 = false;
		cout << "Case #" << all-t << ": ";
		vector < vector <char> > v (6, vector <char> (6, '.'));
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				cin >> v [i][j];
				if (v [i][j] == '.')
					flag1 = true;
			}
		vector < vector <char> > vv (10, vector <char> (4));
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				vv [i][j] = v [i][j];
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				vv [i+4][j] = v [j][i];
		for (int i = 0; i < 4; ++i)
			vv [8][i] = v [i][i];
		for (int i = 0; i < 4; ++i)
			vv [9][i] = v [i][3-i];
		for (int i = 0; i < 10; ++i)
			sort (vv [i].begin (), vv [i].end ());
		for (int i = 0; (i < 10) && (!flag); ++i)
		{
			int c1 = 0, c2 = 0, c3 = 0;
			for (int j = 0; j < 4; ++j)
				if (vv [i][j] == 'O')
					++c1;
				else if (vv [i][j] == 'X')
					++c2;
				else if (vv [i][j] == 'T')
					++c3;
			if (c1 + c3 == 4)
			{
				cout << "O won" << endl;
				flag = true;
			}
			else if (c2 + c3 == 4)
			{
				cout << "X won" << endl;
				flag = true;
			}
		}
		if (flag == true)
			continue;
		else if (flag1 == true)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}
}