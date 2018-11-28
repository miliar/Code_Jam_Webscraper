#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int runs;
long long L, P, C;

int main()
{
	freopen("b_large.in", "r", stdin);
	freopen("b_large.out", "w", stdout);
	
	cin >> runs;
	for (int run = 1; run <= runs; ++run)
	{
		cin >> L >> P >> C;

		int count = 0;
		long long L1 = L;
		while (L1 < P)
		{
			L1 *= C;
			count++;
		}
		count = (int)(ceil(log((double)count) / log(2.0)) + 0.01);

		cout << "Case #" << run << ": " << count << endl;
	}
}
