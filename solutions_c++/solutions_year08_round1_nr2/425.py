#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
using namespace std;
int main()
{
	int c;
	cin>>c;
	for (int i = 0; i < c; ++i)
	{
		int n,m;
		cin>>n>>m;
		vector<vector<int> > customer(m, vector<int>(n, -1));
		
		for (int j = 0; j < m; ++j)
		{
			int t;
			cin>>t;
			for (int k = 0; k < t; ++k)
			{
				int x,y;
				cin>>x>>y;
				customer[j][x-1] = y;
			}
		}

		int ans = 20005;
		int cu = 0;
		int ub = (int)pow(2.0, n);

		for (int b = 0; b < ub; ++b)
		{
			vector<int> sat(m, 0);
			int sa = 0;
			int ca = 0;
			for (int j = 0; j < n; ++j)
			{
				if (((1 << j) & b) != 0)
				{
					++ca;
					for (int k = 0; k < m; ++k)
					{
						if (sat[k] == 0)
						{
							if (customer[k][j] == 1)
							{
								sat[k] = 1;
								++sa;
							}
						}
					}
				}
				else
				{
					for (int k = 0; k < m; ++k)
					{
						if (sat[k] == 0)
						{
							if (customer[k][j] == 0)
							{
								sat[k] = 1;
								++sa;
							}
						}
					}
				}
			}
			if (sa == m && ca < ans)
			{
				ans = ca;
				cu = b;
			}
		}
		if (ans == 20005)
		{
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": ";
			for (int j = 0; j < n; ++j)
			{
				if (((1 << j) & cu) != 0)
				{
					cout<<1;
				}
				else
				{
					cout<<0;
				}

				if (j == n-1)
				{
					cout<<endl;
				}
				else
				{
					cout<<" ";
				}
			}
		}
		
	}
	return 0;
}