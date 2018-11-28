#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
	vector<int> x;
	vector<int> y;
	int c, n, tmp, min;
	cin>>c;
	for (int i = 1; i <= c; ++i)
	{
		cin>>n;
		x.clear();
		y.clear();
		for (int j = 0; j < n; ++j) 
		{
			cin>>tmp;
			x.push_back(tmp);
		}
		for (int j = 0; j < n; ++j) 
		{
			cin>>tmp;
			y.push_back(tmp);
		}
		sort(x.begin(), x.end());
		sort(y.rbegin(), y.rend());
		min = 0;
		for (int j = 0; j < n; ++j)
		{
			min += (x[j]*y[j]);
		}
		cout<<"Case #"<<i<<": "<<min<<endl;
	}
}