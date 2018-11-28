#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <cmath>
#include <cassert>
#include <memory.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define _(a,b) memset((a), (b), sizeof(a))

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int a[1005];
long long res;
int n, k, r;

void solve(int tt)
{
	int s, i, j, p;
	cin >> r >> k >> n;
	for (i = 0; i < n; i++)
		cin >> a[i];
	res = 0;
	p = 0;
	for (i = 0; i < r; i++)
	{
		s = 0;
		for (j = 0; j < n; j++)
		{
			//cout << a[(j + p) % n] << endl;
			if (s + a[(j + p) % n] <= k)
				s += a[(j + p) % n];
			else
				break;
		}
		//cout << endl;
		res += s;
		p = j + p;
	}
	cout << "Case #" << tt + 1 << ": " << res << endl;
}

int main()
{
	prepare();
	int i, t;
	cin >> t;
	for (i = 0; i < t; i++)
		solve(i);
	return 0;
}