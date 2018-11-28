#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <cmath>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <algorithm>
#include <fstream>

using namespace std;

int ones(int i)
{
	int j = 0; while (i) {i &= i-1; ++j;}
	return j;
}

int could[1024][1024] = {0};

void fill()
{
	for (int i = 0; i < 1024; ++i)
	{
		int a[10] = {0};
		for (int k = 0; k < 10; ++k)
			if (i & (1<<k)) a[k] = 1;
		for (int j = 0; j < 1024; ++j)
		{
			bool ok = true;
			for (int k = 0; k < 10; ++k)
				if (j & (1<<k))
				{
					if (!((k == 0 || a[k-1] == 0) && (k == 9 || a[k+1] == 0)))
					{
						ok = false;
						break;
					}
				}
			if (ok) could[i][j] = 1;
		}
	}
}

int main()
{
	ifstream ifs("c.in");
	ofstream ofs("c.out");
	int t;
	ifs >> t;
	fill();
	for (int l =0; l < t; ++l )
	{
		int n,m;
		ifs >> n >> m;
		vector<string> s(n);
		for (int i = 0; i < n; ++i)
			ifs >> s[i];
		vector<int> rows(n);
		for (int i = 0; i < n; ++i)
		{
			int sum = 0;
			for (int j = 0; j < m; ++j)
			{
				sum *= 2;
				sum += int(s[i][j] == 'x');
			}
			rows[i] = sum;
		}
		vector<int> valid;
		for (int i = 0; i < (1<<m); ++i)
		{
			vector<int> pos;
			for (int j = 0; j < 32; ++j)
				if (i & (1<<j))
				{
					pos.push_back(j);
				}
			bool ok = true;
			for (int j = 1; j < pos.size(); ++j)
				if (pos[j]-pos[j-1] == 1)
				{
					ok = false;
					break;
				}
			if (ok) valid.push_back(i);
		}
		int f[10][1024] = {0};
		for (int i = 0; i < valid.size(); ++i)
		{
			if ((valid[i] & rows[0]) == 0)
			{
				f[0][valid[i]] = ones(valid[i]);
			}
		}

		for (int i = 0; i+1 < n; ++i)
		{
			for (int j = 0; j < valid.size(); ++j)
			{
				if (f[i][valid[j]] > 0)
				{
					for (int k = 0; k < valid.size(); ++k)
					{
						if ((valid[k] & rows[i+1]) == 0 && could[valid[j]][valid[k]])
						{
							f[i+1][valid[k]] = max(f[i+1][valid[k]], f[i][valid[j]]+ones(valid[k]));
						}
					}
				}
			}
		}
		int res = *max_element(f[n-1], f[n-1]+(1<<m));
		ofs << "Case #" << l+1 << ": " << res << endl; 
	}

  	return 0;
}
