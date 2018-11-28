// acm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	
	for (int test = 1; test <= t; ++test) {
		int n;
		cin >> n;
		int m = 1000000000, xo, s = 0;
		for (int i = 0; i < n; ++i) {
			int x;
			cin >> x;
			m = min(x, m);
			if (i)
				xo ^= x;
			else
				xo = x;
			s += x;
		}
		cout << "Case #" << test << ": ";
		if (xo)
			cout << "NO\n";
		else
			cout << s - m << '\n'; 
	}

	return 0;
}

