#define fr(i, a, x) for(int(i) = a; i <= x; ++i)
#define rfr(i, a, x) for(int(i) = a; i >= x; --i)
#define all(a) a.begin(), a.end()
#define Min(a, b) (a < b) ? a : b
#define Max(a, b) (a > b) ? a : b
#define pb push_back
#define MY_DEBUG 1

#include <fstream>
#include <cstdio>
#include <string>
#include <map>
#include <ctime>
#include <stack>
#include <deque>
#include <cstdlib>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

#ifdef MY_DEBUG
ifstream cin("input.txt");
ofstream cout("output.txt");
#else 
ifstream cin("j.dat");
ofstream cout("j.ans");
#endif

const double pi = acos(-1.0);
const int inf = 1e9;
const long long linf = 1e18;
const int prost = 51;

int main()
{
	freopen("output.txt", "w", stdout);
	int counttest;
	cin >> counttest;
	for(int test = 1; test <= counttest; ++test)
	{
		long long n, pd, pg;
		bool ans;
		cin >> n >> pd >>  pg;
		if (pg == 0)
		{
			if (pd == 0)
				ans = true;
			else
				ans = false;
		}
		else if (pg == 100)
		{
			if (pd == 100)
				ans = true;
			else
				ans = false;
		}
		else
		{
			long long u = 100, y = 100;
			for(int i = 100; i > 1; --i)
				if (pd % i == 0 && u % i == 0)
				{
					pd /= i;
					u /= i;
				}
			if (u <= n)
				ans = true;
			else
				ans = false;
		}
		if (ans)
			cout << "Case #" << test << ": Possible\n";
		else
			cout << "Case #" << test << ": Broken\n";
	}
	return 0;
}