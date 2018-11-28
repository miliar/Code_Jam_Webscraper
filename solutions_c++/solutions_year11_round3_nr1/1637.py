
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <list>
#include <algorithm>

using namespace std;


int main()
{
	ifstream in("A-large.in");
	ofstream out("A_large.out");

	int T;
	in >> T;

	for (int i=0; i<T; ++i)
	{
		char pic[50][50];
		int R, C;
		in >> R;
		in >> C;

		for (int j=0; j<R; ++j)
		{
			for (int k=0; k<C; ++k)
			{
				char a;
				in >> a;
				pic[j][k] = a;
			}
		}

		bool possible=true;

		for (int j=0; j<R-1; ++j)
		{
			for (int k=0; k<C-1; ++k)
			{
				if (pic[j][k] == '#')
				{
					if (pic[j][k+1] == '#' && pic[j+1][k] == '#' && pic[j+1][k+1] == '#')
					{
						pic[j][k] = '/';
						pic[j][k+1] = '\\';
						pic[j+1][k] = '\\';
						pic[j+1][k+1] = '/';
					}
					else
					{
						possible = false;
						break;
					}
				}
				if (!possible)
				{
					break;
				}
			}
		}

		for (int k=0; k<C; ++k)
		{
			if (pic[R-1][k] == '#')
			{
					possible = false;
					break;
			}
		}
		for (int k=0; k<R; ++k)
		{
			if (pic[k][C-1] == '#')
			{
					possible = false;
					break;
			}
		}

		cout << "Case #" << i+1 << ":" << endl;
		out << "Case #" << i+1 << ":" << endl;
		if (possible)
		{
			for (int j=0; j<R; ++j)
			{
				for (int k=0; k<C; ++k)
				{
					cout << pic[j][k];
					out << pic[j][k];
				}
				cout << endl;
				out << endl;
			}
		}
		else
		{
			cout << "Impossible" << endl;
			out << "Impossible" << endl;
		}
	}

	return 0;
}
