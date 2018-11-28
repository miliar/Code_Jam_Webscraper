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

int n, k;
int a[2000];

int mstep(int cur, long long& s)
{
	int i = cur;
	s = 0;
	do {
		if (s + a[i] <= k)
		{
			s += a[i];
			i = (i+1) % n;
		}
		else break;
	} while (i != cur);
	return i;
}

int main()
{
	ifstream ifs("c.in");
	ofstream ofs("c.out");	
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		int r;
		ifs >> r >> k >> n;	
		for (int i=0; i < n; ++i)
			ifs >> a[i];
		vector<int> step(n, -1);
		vector<long long> sum(n, 0);
		long long s = 0;
		int cur = 0;
		int st = 0;
		int clen = 0;
		step[0] = 0;
		sum[0] = 0;
		long long csum = 0;
		while (st < r)
		{
			++st;
			long long nsum;
			cur = mstep(cur, nsum);
			s = s + nsum;
			if (step[cur] != -1)
			{
				clen = st - step[cur];
				csum = s - sum[cur];
				break;
			}
			else 
			{
				step[cur] = st;
				sum[cur] = s; 
			}
		}
		if (st < r)
		{
			int cnt = (r-st) / clen;
			s += csum * cnt;
			st += cnt*clen;
			while (st < r)
			{
				++st;
				long long nsum;
				cur = mstep(cur, nsum);
				s += nsum;
			}
		}
		ofs << "Case #" << test+1 << ": " << s << endl; 
	}
	
  	return 0;
}
