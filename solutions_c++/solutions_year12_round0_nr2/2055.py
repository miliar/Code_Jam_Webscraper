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

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		int N, S, p, googlers = 0;
		cin >> N >> S >> p;

		for (int i = 0; i < N; i++)
		{
			int t;
			cin >> t;

			if (t >= 2)
			{
				int z1 = t / 3 + ((t % 3) > 0 ? 1 : 0);
				if (z1 >= p)
					googlers++;
				else if (t <= 28)
				{
					z1 = t / 3 + ((t % 3) > 1 ? 2 : 1);
					if (z1 >= p && S-- > 0)
						googlers++;
				}
			}
			else
			{
				if (t >= p)
					googlers++;
			}
		}

		cout << "Case #" << numCase << ": ";
		cout << googlers;
		cout << "\n";

		numCase++;
	}
	return 0;
}
