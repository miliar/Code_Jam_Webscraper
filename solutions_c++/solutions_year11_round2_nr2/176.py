#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <list>
#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }


int main()
{
	time_t tStart = clock();
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int c, d;
		cin >> c >> d;
		vector<int> p(c);
		vector<int> v(c);
		for(int i = 0; i < c; ++i)
			scanf("%d%d", &p[i], &v[i]);

		vector<int> a;
		for(int i = 0; i < c; ++i)
			for(int j = 0; j < v[i]; ++j)
				a.pb(p[i]);
		sort(a.begin(), a.end());
		int n = a.size();

		LD left = 0.0, right = n * LL(d) + 10;
		for(int i = 0; i < 100; ++i)
		{
			LD mid = (left + right) / 2.0;


			bool ok = true;
			LD last = a[0] - mid;
			for(int j = 1; j < n; ++j)
			{
				LD cur = a[j];
				if(cur - last > d)
					cur = max(cur - mid, last + (LD)d);
				else
					cur = min(cur + mid, last + (LD)d);
				if(cur - last < d)
				{
					ok = false;
					break;
				}
				last = cur;
			}

			if(ok)
				right = mid;
			else
				left = mid;
		}

		LD ans = (left + right) / 2.0;
		cout.precision(6);
		cout.setf(ios::fixed);
		cout << "Case #" << z + 1 << ": " << ans << endl;

	}
	time_t tEnd = clock();
	return 0;
}
#endif

