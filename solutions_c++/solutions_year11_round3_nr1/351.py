// acm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test) {
		int r, c;
		cin >> r >> c;
		string a[50];
		for (int i = 0; i < r; ++i)
			cin >> a[i];

		for (int i = 0; i < r - 1; ++i)
			for (int j = 0; j < c - 1; ++j)
				if (a[i][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j] == '#' && a[i + 1][j + 1] == '#') {
					a[i][j] = '/';
					a[i][j + 1] = '\\';
					a[i + 1][j] = '\\';
					a[i + 1][j + 1] = '/';
			}
		bool nooo = false;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (a[i][j] == '#')
					nooo = true;

		cout << "Case #" << test << ":\n";
		if (nooo)
			cout << "Impossible\n";
		else {
			for (int i = 0; i < r; ++i)
				cout << a[i] << endl;
		}
	}

	return 0;
}

