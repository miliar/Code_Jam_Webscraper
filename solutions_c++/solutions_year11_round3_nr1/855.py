// gj.cpp
//

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned __int64 uint64;

char t[50][50];
int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 i = 0; i < cases; ++i)
	{
		uint r, c;
		cin >> r >> c;

		memset(t, 0, sizeof(t));

		for (uint j = 0; j < r; ++j)
		{
			for (uint k = 0; k < c; ++k)
				cin >> t[j][k];
		}

		bool res = true;
		for (uint j = 0; j < r && res; ++j)
		{
			for (uint k = 0; k < c && res; ++k)
			{
				if (t[j][k] == '#')
				{
					if (k + 1 != c && j + 1 != r)
					{
						t[j][k] = '/';
						if (t[j][k + 1] == '#' && t[j + 1][k] == '#' && t[j + 1][k + 1] == '#')
						{
							t[j][k + 1] = '\\';
							t[j + 1][k] = '\\';
							t[j + 1][k + 1] = '/';
						}
						else
							res = false;
					}
					else
						res = false;
				}
			}
		}

		cout << "Case #" << i + 1 << ":" << endl;

		if (res)
		{
			for (uint j = 0; j < r && res; ++j)
			{
				for (uint k = 0; k < c && res; ++k)
					cout << t[j][k];
				cout << endl;
			}
		}
		else
			cout << "Impossible" << endl;
	}

	return 0;
}
