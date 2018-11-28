#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <ctype.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;



int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	
	cin >> tests;
	map <int, int> v;
	queue<int> bad;
	for (int t = 1; t <= tests; t ++)
	{
		int c;
		cin >> c;
		v.clear();
		for (int i = 0; i < c; i ++)
		{
			int x,y;
			cin >> x >> y;
			v[x] = y;
			if (y >= 2)
				bad.push(x);
		}
		long long res = 0;

		while (!bad.empty())
		{
			int p = bad.front();
			bad.pop();
			int cnt = v[p];
			int moves = cnt/2;
			if (moves == 0)
				continue;

			v[p] -= moves*2;
			res += moves;
			v[p-1] += moves;
			v[p+1] += moves;
			if (v[p-1] >= 2)
				bad.push(p-1);
			if (v[p+1] >= 2)
				bad.push(p+1);
		}

		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
