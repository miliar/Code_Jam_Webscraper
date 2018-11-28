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



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n, k, b, t;
		scanf("%d%d%d%d", &n, &k, &b, &t);
		vector<int> x(n);
		vector<int> v(n);
		for(int i = 0; i < n; ++i)
			scanf("%d", &x[i]);
		for(int i = 0; i < n; ++i)
			scanf("%d", &v[i]);
		for(int i = 0; i < n; ++i)
			for(int j = i + 1; j < n; ++j)
				if(x[i] < x[j])
					swap(x[i], x[j]),
					swap(v[i], v[j]);
		x.pb(b);
		v.pb(0);
		vector<int> next(n + 1);
		next[n] = -1;
		for(int i = 0; i < n; ++i)
		{
			int w = n;
			for(int j = 0; j < n; ++j) if(x[j] > x[i] && v[i] > v[j])
			{
				int a = (x[i] - x[j]);
				int b = (v[w] - v[i]);
				int c = (x[i] - x[w]);
				int d = (v[j] - v[i]);
				if(a * b < c * d)
					w = j;
			}
			next[i] = w;
		}

		vector<int> swaps;
		
		for(int i = 0; i < n; ++i) if((x[n] - x[i]) <= t * v[i]) 
		{
			
			int cnt = 0;
			for(int j = 0; j < n; ++j) if(x[j] > x[i])
			{
				if(x[n] - x[j] > t * v[j])
					cnt++;
			}
			swaps.pb(cnt);
		}
		sort(swaps.begin(), swaps.end());
		if(swaps.size() < k)
			printf("Case #%d: IMPOSSIBLE\n", z + 1);
		else
		{
			int sum = 0;
			for(int i = 0; i < k; ++i)
				sum += swaps[i];
			printf("Case #%d: %d\n", z + 1, sum);
		}
	}
	return 0;
}
#endif