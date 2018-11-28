#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <iomanip>
using namespace std;
typedef double LONG;
int main()
{
	int testCases,i,j,n,x,y;
	vector<double> v1,v2;
	cin >> testCases;
	for(i = 1; i <= testCases; i ++)
	{
		cin >> n;
		v1.clear();
		v2.clear();
		for (j = 0; j < n; j ++)
		{
			cin >> x;
			v1.push_back(x);
		}
		for (j = 0; j < n; j ++)
		{
			cin >> y;
			v2.push_back(y);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end(),greater<double>());
		LONG scalar = 0;
		for (j = 0; j < n; j ++)
		{
			scalar += (LONG)v1[j]* (LONG)v2[j];
		}
		cout << "Case #" << i << ": " << fixed << setprecision(0) << scalar << "\n";
	}
	return 0;
}