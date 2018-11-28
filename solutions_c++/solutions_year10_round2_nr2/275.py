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

int main()
{
	ifstream ifs("b.in");
	ofstream ofs("b.out");		
	int c;
	ifs >> c;
	for (int test = 0; test < c; ++test)
	{
		int n,k,b,t;
		ifs >> n >> k >> b >> t;
		vector<int> x(n), v(n);
		for (int i = 0; i < n; ++i)
			ifs >> x[i];
		for (int i =0; i < n; ++i)
			ifs >> v[i];
		int res = 0, cnt = 0, cntg = 0;
		for (int i = n-1; i >= 0 && cntg < k; --i)
		{
			if (b-x[i] <= t*v[i])
			{
				res += cnt;
				++cntg;
			}
			else ++cnt;
		}
		
		if (cntg == k)
			ofs << "Case #" << test+1 << ": " << res << endl;
		else 
			ofs << "Case #" << test+1 << ": " << "IMPOSSIBLE\n";
	}
  	return 0;
}
