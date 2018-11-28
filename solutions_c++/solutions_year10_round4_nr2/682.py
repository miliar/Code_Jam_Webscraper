#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int a[12][1026];
int m[1026];
int mem[12][1026][12];

int run(int vi, int vj, int skip)
{
	if (mem[vi][vj][skip] != -1)
		return mem[vi][vj][skip];

	if (vi == 0)
	{
			if ( m[2*vj] < skip || m[2*vj + 1] < skip)
				return 1000000000; //???
			if (m[2*vj] == skip || m[2*vj + 1] == skip)
				return a[vi][vj];
			else
				return 0;
	}
	int r = min( run(vi-1, 2*vj, skip + 1) + run(vi-1, 2*vj+1, skip + 1), run(vi-1, 2*vj, skip) + run(vi-1, 2*vj+1, skip) + a[vi][vj] );
	if (r > 1000000000) 
		r = 1000000000;
	mem[vi][vj][skip] = r;
	return r;
}

int main()
{
	int testCnt;
	cin >> testCnt;

	for (int T = 0; T < testCnt; ++T)
	{
		memset(mem, -1, sizeof mem);
		int p;
		cin >> p;
		for (int i = 0; i < (int)pow(2.0, (double)p); ++i)
			cin >> m[i];
		for (int i = p-1; i >= 0; --i)
		{
			for (int j = 0; j < (int)pow(2.0, (double)i); ++j)
			{
				cin >> a[p-1-i][j];
			}
		}

		int res = run(p-1, 0, 0);
		
		cout << "Case #" << T+1 << ": " << res << endl;
	}

	return 0;
}