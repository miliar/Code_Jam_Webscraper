#include <cstdio>
#include <vector>
#include <utility>
#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <limits.h>
#include <time.h>
#include <iomanip>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <list>
#include <stack>
using namespace std;
typedef int LL;


void Solve()
{
	int n;
	vector<int> v;
	cin >> n;
	v.resize(n);
	int f = 0;
	int l = INT_MAX;
	int s = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> v[i];
		f = f^v[i];
		s += v[i];
		if (v[i] < l)
			l = v[i];
	}
	if (f != 0)
	{
		cout << "NO";
		return;
	}
	else
		cout << s - l;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	cin >> t; 
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ": ";
		Solve();
		cout << endl;
	}

	return 0;
}