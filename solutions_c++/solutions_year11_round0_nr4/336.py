/*
 * c.cpp
 *
 *  Created on: 2011-5-7
 *      Author: acer
 */


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;


int array[1024];
int gone[1024];

int findloop(int p)
{
	if (gone[p]) return 0;
	gone[p] = true;
	return findloop(array[p]) + 1;
}

double count(int s)
{
	if (s <= 1) return 0.0;
	return (double)s;
}

int main()
{
	int tn;
	cin >> tn;
	cout.precision(6);
	for (int ti = 1; ti <= tn; ++ti)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			cin >> array[i];
			--array[i];
		}

		memset(gone, false, sizeof(gone));


		double s = 0;
		for (int i = 0; i < n; ++i)
		{
			s += count(findloop(i));
		}
		cout << "Case #" << ti << ": ";
		printf("%.6lf\n", s);
	}
	return 0;
}
