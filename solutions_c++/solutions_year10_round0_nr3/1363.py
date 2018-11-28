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
	OpenSmall("C");
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		long long r, k, n;
		cin >> r >> k >> n;
		deque<long long> g;
		for(int i = 0; i < n; ++i)
		{
			long long gi;
			cin >> gi;
			g.push_back(gi);
		}
		long long ans = 0;
		for(int i = 0; i < r; ++i)
		{
			long long cnt = 0;
			deque<long long> g1 = g;
			while(!g.empty() && cnt + g.front() <= k)
			{
				long long frnt = g.front();
				cnt += frnt;
				g.pop_front();
				g1.pop_front();
				g1.push_back(frnt);
			}
			g = g1;
			ans += cnt;
		}
		cout<<"Case #"<<Case+1<<": ";
		cout << ans << endl;
	}

	return 0;
}