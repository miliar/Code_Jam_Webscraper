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
#include <numeric>

using namespace::std;

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		int L, N, C;
		long long t;
		cin >> L;
		cin >> t;
		cin >> N >> C;

		std::vector<long long> buf;
		buf.reserve(N);
		for (int i = 0; i < N; i++)
		{
			long long d;
			if (i < C)
				cin >> d;
			else
				d = buf[i % C] / 2;
			buf.push_back(d * 2);
		}

		if (L == 0)
			t = 0;

		int k = 0;
		long long m = t;
		while (k < N && m >= buf[k])
			m -= buf[k++];
		if (k < N)
		{
			buf[k] -= m;
			buf.erase(buf.begin(), buf.begin() + k);
			std::sort(buf.begin(), buf.end());
			for (std::vector<long long>::reverse_iterator itr = buf.rbegin(); itr != buf.rend() && L-- > 0; itr++)
				*itr /= 2;

			long long s = 0;
			t += std::accumulate(buf.begin(), buf.end(), s);
		}

		cout << "Case #" << numCase << ": ";
		cout << t;
		cout << "\n";

		numCase++;
	}
	return 0;
}
