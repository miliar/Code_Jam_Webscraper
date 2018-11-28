// 2012_Q_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <string>
#include <map>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;



int _tmain(int argc, _TCHAR* argv[]) {
	size_t T = 0;
	cin >> T;
	for (size_t i = 0; i < T; ++i) {
		size_t N = 0;
		cin >> N;
		size_t S = 0;
		cin >> S;
		size_t p = 0;
		cin >> p;
		size_t clear = 0;
		size_t surprise = 0;
		for (int j = 0; j < N; ++j) {
			size_t value;
			cin >> value;
			if (0 == p)
				clear++;
			else if (value >= p) {
				const size_t diff = value - p;
				const size_t smallest = diff/2;
				if (smallest >= p || (p-smallest) == 1 )
					clear++;
				else if ((p-smallest) == 2)
					surprise++;
			}
		}
		size_t count = clear + ((surprise > S) ? S : surprise);
		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}

