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
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	
	cin >> tests;

	for (int t = 1; t <= tests; t ++)
	{
		long long l,n;
		cin >> l >> n;
		vector <long long> b(n);
		for (int i = 0; i < n ;i ++)
			cin >> b[i];

		vector <long long> sum(100000,-1);
		sum[0] = 0;
		for (int i = 0; i < n; i ++)
			sum[b[i]] = 1;
		for (int i = 0; i < sum.size(); i ++)
		{
			if (sum[i] == -1)
				continue;
			for (int j = 0; j < n; j ++)
			{
				long long r = i+b[j];
				if (r< sum.size() && (sum[r] == -1 || sum[r] > sum[i]+1))
					sum[r] = sum[i]+1;
			}
		}
		long long res = -1;
		for (int i = 0; i <n; i ++)
		{
			long long r = l/b[i];
			long long nres = r;
			r = r*b[i];
			while (l-r < sum.size()-1)
			{
				if (sum[l-r] != -1)
				{
					if (res == -1 || res > nres+sum[l-r])
						res = nres+sum[l-r];
				}
				r-=b[i];
				nres--;
			}
		}

		if (res == -1)
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
