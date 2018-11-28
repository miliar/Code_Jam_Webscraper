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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void OpenSmall(string leter)
{
	string inName = leter + "-small.in";
	string outName = leter + "-small.out";
	freopen(inName.c_str(), "r", stdin);
	freopen(outName.c_str(), "w", stdout);
}

void OpenLarge(string leter)
{
	string inName = leter + "-large.in";
	string outName = leter + "-large.out";
	freopen(inName.c_str(), "r", stdin);
	freopen(outName.c_str(), "w", stdout);
}

int pow2(int n)
{
	int ans = 1;
	for(int i = 0; i < n; ++i)
		ans <<= 1;
	return ans;
}

int main()
{
	OpenLarge("B");
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int n, k, b, t;
		cin >> n >> k >> b >> t;
		vector<int> x(n);
		vector<int> v(n);
		for(int i  = 0; i < n; ++i)
			cin >> x[i];
		for(int i  = 0; i < n; ++i)
			cin >> v[i];
		int cnt = 0;
		int ans = 0;
		for(int i = n-1; i >= 0 && cnt < k; --i)
		{
			if((b - x[i])%v[i] == 0 && (b - x[i])/v[i] > t || (b - x[i])%v[i] != 0 && (b - x[i])/v[i] >= t)
			{
				ans += (k - cnt);
			}
			else
				++cnt;
		}
		cout<<"Case #"<<Case+1<<": ";
		if(cnt == k)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}