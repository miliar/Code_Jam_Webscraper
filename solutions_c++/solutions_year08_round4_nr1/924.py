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

const int INF = 100000;

int main()
{
	int n;
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		int m,v;
		cin>>m>>v;
		vector<int> nodes(m+1, 0);
		vector<int> changable(m+1, 0);

		vector<int> minV40(m+1, INF);
		vector<int> minV41(m+1, INF);

		for (int j = 1; j <= (m-1)/2; ++j)
		{
			cin>>nodes[j];
			cin>>changable[j];
		}

		for (int j = (m-1)/2 + 1; j <= m; ++j)
		{
			cin>>nodes[j];
		}

		for (int j = m; j > (m-1)/2; --j)
		{
			if (nodes[j] == 0)
			{
				minV40[j] = 0;
				minV41[j] = INF;
			}
			else
			{
				minV40[j] = INF;
				minV41[j] = 0;
			}
		}

		for (int j = (m-1)/2; j > 0; --j)
		{
			int p = j;
			int l = 2*j;
			int r = l + 1;
			if (nodes[p] == 0)
			{
				int tmp1 = min(minV40[r] + minV41[l], minV41[r] + minV40[l]);
				int tmp2 = min(minV41[r] + minV41[l], tmp1);

				minV41[p] = tmp2;

				minV40[p] = minV40[r] + minV40[l];
				if (changable[p] == 1)
				{
					minV40[p] = min(tmp1 + 1, minV40[p]);
				}
			}
			else
			{
				int tmp1 = min(minV40[r] + minV41[l], minV41[r] + minV40[l]);
				int tmp2 = min(minV40[r] + minV40[l], tmp1);

				minV40[p] = tmp2;

				minV41[p] = minV41[r] + minV41[l];
				if (changable[p] == 1)
				{
					minV41[p] = min(tmp1 + 1, minV41[p]);
				}
			}
		}

		if (v == 0)
		{
			if (minV40[1] < INF)
			{
				cout<<"Case #"<<i+1<<": "<<minV40[1]<<endl;
			}
			else
			{
				cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
			}
		}
		else
		{
			if (minV41[1] < INF)
			{
				cout<<"Case #"<<i+1<<": "<<minV41[1]<<endl;
			}
			else
			{
				cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
			}
		}

	}
	return 0;
}