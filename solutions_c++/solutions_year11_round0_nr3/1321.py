#include <iostream>
#include <algorithm>
#include <numeric>
#include <cstdio>
using namespace std;

const int N = 1000 + 10;
int c[N];
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int testcase = 1; testcase <= T; testcase++)
	{
		int n;
		cin >> n;
		int tmp = 0;
		for (int i = 1; i <= n; i++)
		{
			cin >> c[i];
			tmp ^= c[i];
		}
		cout << "Case #" << testcase << ": ";
		if (tmp != 0)
		{
			cout << "NO" << endl;
		}
		else
		{
			sort(c+1, c+1+n);
			cout << accumulate(c+2, c+1+n, 0) << endl;
		}
	}
}
