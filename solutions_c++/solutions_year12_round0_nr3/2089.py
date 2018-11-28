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

int recycle(int x, int mult)
{
	int a = x % mult;
	x /= mult;

	if (a == 0)
		return x;

	int t = x;
	while (t > 0)
	{
		t /= 10;
		a *= 10;
	}

	return a + x;
}

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	std::set<int> setUnique;

	while (numCase <= nCount)
	{
		int A, B;
		cin >> A >> B;

		int numbers = 0;

		for (int n = A; n < B; n++)
		{
			setUnique.clear();

			int x = n;
			for (int q = 10; q <= x; q *= 10)
			{
				int y = recycle(x, q);
				if (x < y && y <= B)
				{
					setUnique.insert(y);
				}
			}

			numbers += setUnique.size();
		}

		cout << "Case #" << numCase << ": ";
		cout << numbers;
		cout << "\n";

		numCase++;
	}
	return 0;
}
