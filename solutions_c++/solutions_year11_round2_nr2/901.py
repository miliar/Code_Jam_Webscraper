#define fr(i, a, x) for(int(i) = a; i <= x; ++i)
#define rfr(i, a, x) for(int(i) = a; i >= x; --i)
#define all(a) a.begin(), a.end()
#define Min(a, b) (a < b) ? a : b
#define Max(a, b) (a > b) ? a : b
#define pb push_back
#define MY_DEBUG 1

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
#include <fstream>
ifstream cin("input.txt");
ofstream cout("output.txt");
#else 
#include <iostream>
#endif

const double pi = acos(-1.0);
const double eps = 1e-9;
const int inf = 1e9;
const long long linf = 1e18;
const int prost = 51;

struct tree
{
	tree * l, * r;
	int x, y, count;
};	

int main()
{
#ifdef MY_DEBUG
	freopen("output.txt", "w", stdout);
#endif
	int counttest;
	cin >> counttest;
	for(int test = 1; test <= counttest; ++test)
	{
		int n;
		double d;
		cin >> n >> d;
		vector<int> pos;
		for(int i = 0, x, c; i < n; ++i)
		{
			cin >> x >> c;
			for(int j = 0; j < c; ++j)
				pos.push_back(x);
		}
		sort(pos.begin(), pos.end());
		double ans = 0, t;
		int m = pos.size();
		for(int i = 0; i < m - 1; ++i)
		{
			if (pos[i + 1] - pos[i] > d - eps)
				continue;
			t = (pos[i] + d - pos[i + 1]) / 2;
			if (t > ans)
				ans = t;
			pos[i + 1] = pos[i] + d;
		}
		printf("Case #");
		printf("%l: ", test);
		printf("%.9f\n", ans);
		//cout << "Case #" << test << ": " << ans << '\n';
	}
}