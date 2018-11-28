#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	

	int cntTest;
	cin >> cntTest;

	for (int test = 0; test < cntTest; ++test)
	{
		int n;
		cin >> n;
		vector <int> perm(n);
		vector < vector <int> > p(n);
		vector <bool> used(n);
		int size = 0;

		for (int i = 0; i < n; ++i)
		{
			cin >> perm[i];
			--perm[i];
		}

		for (int i = 0; i < n; ++i)
		{
			if (used[ i ])
				continue;

			used[ i ] = true;
			int next = perm[i];
			p[size].push_back( i );

			while (!used[ next ])
			{
				p[size].push_back( next );
				used[next] = true;
				next = perm[next];				
			}

			++size;
		}

			double res = 0;
			for (int i = 0; i < size; ++i)
				res += (p[i].size() > 1 ? p[i].size() : 0);

		printf("Case #%d: %.10lf\n", test + 1, res);
	}

	return 0;
}


