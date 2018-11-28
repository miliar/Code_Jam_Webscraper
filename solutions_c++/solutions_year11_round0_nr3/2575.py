// CandySplitting.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream> 

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for (int ncase = 1; ncase <= T; ++ncase) {
		int n;
		cin >> n;
		int sum = 0;
		int xor = 0;
		int min = 100000000;
		for (int i = 0; i < n; ++i) {
			int x;
			cin >> x;
			sum += x;
			xor ^= x;
			if (min > x)
				min = x;
		}
		cout << "Case #" << ncase << ": ";
		if (xor == 0)
			cout << sum - min << endl;
		else
			cout << "NO" << endl;
	}
	return 0;

}

