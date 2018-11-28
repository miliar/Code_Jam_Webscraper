#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <fstream>
#include <memory.h>
#include <algorithm>

using namespace std;

const int M = 20000;
int f[M];
const long long maxl = 1000000000000000001LL;

int main()
{
	ifstream ifs("b.in");
	ofstream ofs("b.out");	
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		memset(f, -1, sizeof(f));
		f[0] = 0;
		long long l;
		int n;
		ifs >> l >> n;
		vector<int> a(n);
		for (int i = 0; i < n; ++i)
		{
			ifs >> a[i];
		}
		sort(a.begin(), a.end());
		for (int i = 0; i < n; ++i)
		{
			int num = a[i];
			for (int j = num; j < M; ++j)
			{
				int prev = f[j-num];
				if (prev != -1 && (f[j] == -1 || f[j] > prev+1))
				{
					f[j] = prev+1;
				}
			}
		}
		long long res = maxl;
		for (int i = 0; i < M; ++i)
		{
			if (f[i] != -1 && (l-i) % a.back() == 0)
			{
				res = min<long long>(res, f[i]+(l-i)/a.back());
			}
		}
		if (res == maxl)
		{
			ofs << "Case #" << test+1 << ": " << "IMPOSSIBLE" << endl;
		}
		else 
		{
			ofs << "Case #" << test+1 << ": " << res << endl;
		}
	}
  	return 0;
}
