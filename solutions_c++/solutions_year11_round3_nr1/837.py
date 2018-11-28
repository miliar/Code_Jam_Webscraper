#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;

int R, C;
char arr[512];

char cget(int r, int c)
{
	if (r < 0 || r >= R || c < 0 || c >= C)
		return 0;
	return arr[r * C + c];
}

void cset(int r, int c, char a)
{
	if (r < 0 || r >= R || c < 0 || c >= C)
		return;
	arr[r * C + c] = a;
}

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		cout << "Case #" << numCase << ": \n";

		cin >> R >> C;

		for (int i = 0; i < R; i++)
		{
			cin >> arr + i * C;
		}

		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				int a = cget(r, c);
				if (a == '#')
				{
					if (cget(r, c + 1) == '#' && cget(r + 1, c) == '#' && cget(r + 1, c + 1) == '#')
					{
						cset(r, c,     '/');  cset(r, c + 1,     '\\');
						cset(r + 1, c, '\\'); cset(r + 1, c + 1, '/') ;
					}
				}
			}
		}

		char* pEnd = arr + R * C;
		if (std::find(arr, pEnd, '#') != pEnd)
			cout << "Impossible\n";
		else
		{
			for (int r = 0; r < R; r++)
			{
				for (int c = 0; c < C; c++)
					cout << cget(r, c);
				cout << "\n";
			}

		}

		numCase++;
	}
	return 0;
}
