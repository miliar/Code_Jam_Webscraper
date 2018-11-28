//#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

void main()
{
	ifstream f;
	f.open("in.txt");
	if (f.fail())
	{
		cout << "cannot open file" << endl;
		return;
	}

	int cases = 0;
	f >> cases;
	char table[60][60];
	for (int _case=1; _case<=cases; _case++)
	{
		int h, w;
		f >> h;
		f >> w;
		string s;

		getline(f, s);
		cout << "Case #" << _case << ": " << endl;
		for (int y=0; y<h; y++)
		{
			getline(f, s);
			for (int i=0; i<w; i++)
				table[i][y] = s[i];
		}

		bool possible = true;
		for (int y=0; y<h && possible; y++)
		for (int x=0; x<w && possible; x++)
			if (table[x][y] == '#')
				if (x == w-1 || y == h-1)
					possible = false;
				else
				{
					if (table[x+1][y]!='#' || table[x][y+1]!='#' || table[x+1][y+1]!='#')
						possible = false;
					table[x][y] = '/';
					table[x+1][y] = '\\';
					table[x][y+1] = '\\';
					table[x+1][y+1] = '/';
				}

		if (!possible)
			cout << "Impossible" << endl;
		else
		{
			for (int y=0; y<h && possible; y++)
			{
				for (int x=0; x<w && possible; x++)
					cout << table[x][y];
				cout << endl;
			};
		}
	}
}
