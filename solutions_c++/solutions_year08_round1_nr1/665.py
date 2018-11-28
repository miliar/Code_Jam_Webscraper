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
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		int n;
		cin>>n;
		vector<int> a(n);
		vector<int> b(n);

		for (int j = 0; j < n; ++j)
		{
			cin>>a[j];
		}
		for (int j = 0; j < n; ++j)
		{
			cin>>b[j];
		}

		sort(a.begin(), a.end());
		sort(b.rbegin(), b.rend());

		long long ans = 0;

		for (int j = 0; j < n; ++j)
		{
			ans += a[j]*b[j];
		}

		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}