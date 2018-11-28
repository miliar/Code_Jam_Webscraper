#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int i = 0;i<T;i++)
	{
		int n;
		cin>>n;
		vector<int> x;
		vector<int> y;
		for(int j=0;j<n;j++)
		{
			int v;
			cin>>v;
			x.push_back(v);
		}
		for(int j=0;j<n;j++)
		{
			int v;
			cin>>v;
			y.push_back(v);
		}

		sort(x.begin(), x.end());
		sort(y.begin(), y.end());

		int p =0;
		for(int j=0;j<n;j++)
		{
			p += x[j] * y[n-j-1];
		}

		printf("Case #%d: %d\n", i+1, p);
	}

	return 0;
}
