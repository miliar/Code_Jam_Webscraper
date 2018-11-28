// Hotdogs.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for (int ncase = 1; ncase <= T; ++ncase) {
		int d, c;
		cin >> c >> d;
		vector<int> x;
		for (int i = 0; i < c;++i) {
			int p, v;
			cin >> p >> v;
			for (int j = 0; j < v; ++j)
				x.push_back(p);
		}
		vector<int> s;
		for (int i = 0; i < x.size(); ++i)
			s.push_back(x[i] - x[0] - i * d);
		if (s.size() == 0) {
			cout << "Case #" << ncase << ": 0.0" << endl;
			continue;
		}
		int res = 0;
		for (int i = 0; i < s.size(); ++i)
			for (int j = i + 1; j < s.size(); ++j) 
				if (s[i] > s[j])
					res = max(s[i] - s[j], res);
		cout << "Case #" << ncase << ": " << (double) res / 2.0 << endl;
	}
	return 0;
}

