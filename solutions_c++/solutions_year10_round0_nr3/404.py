// #pragma comment(linker, "/stack:128000000")
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

typedef long double ld;
typedef long long i64;
typedef pair <int, int> PII;

int g[2048];
int ans[1024];
int next[1024];
int n, r, k, tcn;

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cin >> tcn;
	for (int tc = 1; tc <= tcn; tc++)
	{
		cin >> r >> k >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> g[i];
			g[n + i] = g[i];
		}

		for (int i = 0, j = 0, sum = 0; i < n; i++)
		{
			while (j != i + n && sum + g[j] <= k) sum += g[j++];
			ans[i] = sum;
			next[i] = j >= n ? j - n : j;
			sum -= g[i];
		}

		i64 res = 0;
		int i = 0;
		while (r--)
		{
			res += ans[i];
			i = next[i];
		}
		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}
