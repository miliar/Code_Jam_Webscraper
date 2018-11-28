/*
 * A.cpp
 *
 *  Created on: 2011-5-21
 *      Author: stm
 */

#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	long long Pd, Pg, n;
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> n >> Pd >> Pg;
		if ((Pd < 100 && Pg == 100) || (Pd > 0 && Pg == 0)) {
			cout << "Case #" << t << ": " << "Broken\n";
			continue;
		}
		if ((Pd == 100 && Pg == 100) || (Pd == 0)) {
			cout << "Case #" << t << ": " << "Possible\n";
			continue;
		}
		int c1 = 0, c2 = 0;
		long long x = Pd;
		while (x > 1LL && x % 2LL == 0 && c1 < 2) c1++, x /= 2;
		while (x > 1LL && x % 5LL == 0 && c2 < 2) c2++, x /= 5;
        int m = 1;
        for (int i = 0; i < 2 - c1; ++i) m *= 2;
        for (int i = 0; i < 2 - c2; ++i) m *= 5;
        if (m > n)
        	cout << "Case #" << t << ": " << "Broken\n";
        else
        	cout << "Case #" << t << ": " << "Possible\n";
	}
	return 0;
}
