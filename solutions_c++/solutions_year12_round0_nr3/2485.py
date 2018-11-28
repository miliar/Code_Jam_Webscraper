#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <set>

using namespace std;
set<pair<int, int> > recycled;

int count(int N, int high, int low)
{
	char		a[16], sz, cnt = 0;
	char		b[16];

	sprintf(a, "%d", N);
	sz = strlen(a);
	for (int i = sz - 1; i >= 1; i--)
	{
		int	p, q;
		if (a[i] == '0' || a[i] < a[0])
			continue;
		for (p = i, q = 0; p < sz; p++, q++)
			b[q] = a[p];
		for (p = 0; p < i; p++, q++)
			b[q] = a[p];
		assert(q == sz);
		b[q] = '\0';
		int M = atoi(b);
		if (M > N && M <= high)
		{
			assert (N <= high && N >=low && M >= low);
			recycled.insert(make_pair(N, M));
		}
#		if 0		
		int	p, q;
		if (a[i] == '0' || a[i] > a[0])
			continue;
		for (p = 0, q = i; q < sz; p++, q++)
			if (a[p] > a[q])
				break;
		if (q < sz || a[p] > a[0])
		{
			bool stop = false;
			for (p = 0, q = i; !stop && q < sz; q++, p++)
			{
				if (a[q] < low[p])
					break;
				stop = (a[q] > low[p]);
			}
			if (q < sz)
				continue;
			if (!stop)
			{
				for (q = 0; q < i; q++, p++)
					if (a[q] < low[p])
						break;
				if (q < i)
					continue;
			}
			cnt++;
			print_pairs(a, sz, i);
		}
#		endif
	}
	return cnt;
}

int main()
{
	int		T, nA, nB, ans = 0;
	string		A, B;

	cin >> T;
	for (int caseno = 1; caseno <= T; caseno++)
	{
		cin >> nA >> nB;
		recycled.erase(recycled.begin(), recycled.end());
		for (int i = nA; i <= nB; i++)
			count(i, nB, nA); 
		cout << "Case #" << caseno << ": " << recycled.size() << endl;
	}
	return 0;
}
