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
	int n;
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		int p, k, l;
		cin>>p>>k>>l;
		vector<long long> f(l, 0);
		for (int j = 0; j < l; ++j)
		{
			cin>>f[j];
		}
		sort(f.rbegin(), f.rend());

		long long ans = 0;
		for (int j = 0; j < l; ++j)
		{
			ans += f[j]*(j/k + 1);
		}

		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}