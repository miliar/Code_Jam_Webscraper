#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <functional>
#include <stack>
#include <queue>
#include <string>
#include <memory.h>
#include <iostream>
#include <sstream>

using namespace std;

const int inf = 1000 * 1000 * 1000;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef long long LL;
//typedef double D;

int n, t;
vint V;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		cin >> n;
		V.assign(n, 0);
		int t = 0;
		for(int j = 0; j < n; ++j)
		{
			cin >> V[j];
			t ^= V[j];
		}
		if (t)
		{
			cout << "Case #" << i + 1 << ": NO" << endl;
			continue;
		}
		sort(V.begin(), V.end());
		int res = 0;
		for(int i = 1; i < n; ++i)
			res += V[i];
		cout << "Case #" << i + 1 << ": " << res << endl; 
	}
	return 0;
}